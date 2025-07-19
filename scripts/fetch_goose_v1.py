#!/usr/bin/env python3
"""
Goose data fetcher using elgoose.net API v1.

This script fetches all data from the v1 API and filters for Goose (artist_id=1)
to ensure we get complete setlist coverage including 2023-2025.
"""

import json
import pandas as pd
from pathlib import Path
from collections import Counter

import requests


class ElGooseV1Client:
    """Client for elgoose.net API v1."""
    
    BASE_URL = "https://elgoose.net/api/v1"
    GOOSE_ARTIST_ID = 1
    
    def fetch_all_data(self, endpoint: str) -> list:
        """
        Fetch all data from a v1 endpoint.
        
        Args:
            endpoint: API endpoint (shows, setlists, songs, etc.)
            
        Returns:
            List of all records from the endpoint
        """
        url = f"{self.BASE_URL}/{endpoint}.json"
        
        try:
            print(f"Fetching all {endpoint} from v1 API...")
            print(f"URL: {url}")
            
            response = requests.get(url, timeout=120)
            response.raise_for_status()
            
            result = response.json()
            
            if result.get('error'):
                print(f"API Error: {result.get('error_message', 'Unknown error')}")
                return []
            
            data = result.get('data', [])
            print(f"✓ Retrieved {len(data)} total {endpoint} records")
            
            return data
            
        except Exception as e:
            print(f"✗ Error fetching {endpoint}: {e}")
            return []
    
    def filter_goose_data(self, data: list, endpoint: str) -> list:
        """Filter data for Goose artist only."""
        if not data:
            return []
        
        goose_data = []
        
        for record in data:
            # Check if this is a Goose record
            if (record.get('artist_id') == self.GOOSE_ARTIST_ID or 
                record.get('artist') == 'Goose'):
                goose_data.append(record)
        
        print(f"  Filtered to {len(goose_data)} Goose records (from {len(data)} total)")
        return goose_data


def analyze_year_coverage(data: list, data_type: str) -> None:
    """Analyze year coverage in the data."""
    if not data:
        return
    
    # Find year field
    year_field = None
    sample = data[0] if data else {}
    
    for field in ['show_year', 'showyear', 'year']:
        if field in sample:
            year_field = field
            break
    
    if not year_field:
        print(f"  No year field found in {data_type}")
        return
    
    # Count by year
    year_counts = Counter()
    for record in data:
        year = record.get(year_field)
        if year:
            year_counts[year] += 1
    
    if year_counts:
        years = sorted(year_counts.keys())
        print(f"  Years: {min(years)} - {max(years)}")
        
        # Show recent years specifically
        recent_years = {year: count for year, count in year_counts.items() if year >= 2020}
        if recent_years:
            print(f"  Recent years: {dict(sorted(recent_years.items()))}")
        
        # Check for 2014-2025 coverage
        expected_years = set(range(2014, 2026))
        actual_years = set(years)
        missing_years = expected_years - actual_years
        
        if missing_years:
            print(f"  ⚠️  Missing years: {sorted(missing_years)}")
        else:
            print(f"  ✓ Complete coverage 2014-2025")


def main():
    """Fetch complete Goose data using v1 API."""
    print("Goose Data Fetcher - API v1")
    print("=" * 40)
    
    client = ElGooseV1Client()
    
    # Define paths
    project_root = Path(__file__).resolve().parents[1]
    output_path = project_root / "data" / "v1_goose"
    csv_path = project_root / "data" / "final_v1"
    
    output_path.mkdir(parents=True, exist_ok=True)
    csv_path.mkdir(parents=True, exist_ok=True)
    
    print(f"JSON output: {output_path}")
    print(f"CSV output: {csv_path}")
    
    # Endpoints to fetch
    endpoints = ["shows", "setlists", "songs"]
    
    for endpoint in endpoints:
        print(f"\n🔄 Processing {endpoint.upper()}")
        print("-" * 30)
        
        # Fetch all data
        all_data = client.fetch_all_data(endpoint)
        
        if all_data:
            # Filter for Goose
            goose_data = client.filter_goose_data(all_data, endpoint)
            
            if goose_data:
                # Save JSON
                json_file = output_path / f"goose_{endpoint}.json"
                with open(json_file, 'w', encoding='utf-8') as f:
                    json.dump(goose_data, f, ensure_ascii=False, indent=2)
                print(f"  Saved JSON: {json_file.name}")
                
                # Convert to CSV
                df = pd.DataFrame(goose_data)
                csv_file = csv_path / f"goose_{endpoint}.csv"
                df.to_csv(csv_file, index=False, encoding='utf-8')
                print(f"  Saved CSV: {csv_file.name} ({len(df)} rows × {len(df.columns)} cols)")
                
                # Analyze year coverage
                analyze_year_coverage(goose_data, endpoint)
                
                # Show date range if available
                if 'showdate' in df.columns:
                    dates = df['showdate'].dropna().sort_values()
                    if not dates.empty:
                        print(f"  Date range: {dates.iloc[0]} to {dates.iloc[-1]}")
                
            else:
                print(f"  No Goose data found in {endpoint}")
        else:
            print(f"  No data retrieved for {endpoint}")
    
    print(f"\n🎉 Goose v1 data fetch complete!")
    print(f"📁 JSON files: {output_path}")
    print(f"📁 CSV files: {csv_path}")
    
    # Final summary
    csv_files = list(csv_path.glob("*.csv"))
    if csv_files:
        print(f"\n📊 Final Dataset Summary:")
        total_records = 0
        for csv_file in csv_files:
            try:
                df = pd.read_csv(csv_file)
                total_records += len(df)
                print(f"  • {csv_file.name}: {len(df):,} records")
            except Exception as e:
                print(f"  • {csv_file.name}: Error - {e}")
        
        print(f"\nTotal Goose records: {total_records:,}")


if __name__ == "__main__":
    main()
