#!/usr/bin/env python3
"""
Explorer for elgoose.net API v1 to understand structure and endpoints.

This script tests various v1 endpoints to determine the correct API structure.
"""

import json
import requests
from pathlib import Path


class ElGooseV1Explorer:
    """Explorer for elgoose.net API v1."""
    
    BASE_URL = "https://elgoose.net/api/v1"
    
    def test_endpoint(self, endpoint: str, format_type: str = "json") -> dict:
        """Test a v1 API endpoint."""
        url = f"{self.BASE_URL}/{endpoint}.{format_type}"
        
        try:
            print(f"Testing: {url}")
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            if format_type == "json":
                data = response.json()
                return {"success": True, "data": data, "url": url}
            else:
                return {"success": True, "data": response.text[:500], "url": url}
                
        except Exception as e:
            return {"success": False, "error": str(e), "url": url}


def main():
    """Explore v1 API endpoints to understand structure."""
    print("ElGoose.net API v1 Explorer")
    print("=" * 40)
    
    explorer = ElGooseV1Explorer()
    
    # Test various endpoints that might exist in v1
    endpoints_to_test = [
        "shows",
        "setlists", 
        "songs",
        "venues",
        "artists",
        "jamcharts",
        "latest"
    ]
    
    successful_endpoints = []
    
    for endpoint in endpoints_to_test:
        print(f"\n🔍 Testing {endpoint}")
        print("-" * 25)
        
        # Try JSON format
        result = explorer.test_endpoint(endpoint, "json")
        
        if result["success"]:
            print(f"✓ SUCCESS: {result['url']}")
            data = result["data"]
            
            if isinstance(data, list) and data:
                print(f"  Records: {len(data)}")
                sample = data[0]
                if isinstance(sample, dict):
                    print(f"  Sample fields: {list(sample.keys())[:8]}...")
                    
                    # Look for Goose data
                    goose_count = 0
                    for record in data[:100]:  # Check first 100 records
                        if (record.get('artist') == 'Goose' or 
                            record.get('artist_id') == 1 or 
                            record.get('artist_id') == '1'):
                            goose_count += 1
                    
                    if goose_count > 0:
                        print(f"  Goose records found: {goose_count} in first 100")
                    
            elif isinstance(data, dict):
                print(f"  Response type: dict with keys {list(data.keys())}")
                if 'data' in data and isinstance(data['data'], list):
                    print(f"  Data records: {len(data['data'])}")
            
            successful_endpoints.append(endpoint)
            
        else:
            print(f"✗ FAILED: {result['error']}")
    
    # Summary
    print(f"\n🎯 SUMMARY")
    print("=" * 40)
    
    if successful_endpoints:
        print(f"✓ Working v1 endpoints: {successful_endpoints}")
        
        # Test one successful endpoint with more detail
        if successful_endpoints:
            test_endpoint = successful_endpoints[0]
            print(f"\n📊 Detailed analysis of {test_endpoint}:")
            result = explorer.test_endpoint(test_endpoint, "json")
            
            if result["success"]:
                data = result["data"]
                
                # Save sample data for analysis
                project_root = Path(__file__).resolve().parents[1]
                sample_path = project_root / "data" / "v1_samples"
                sample_path.mkdir(parents=True, exist_ok=True)
                
                sample_file = sample_path / f"{test_endpoint}_v1_sample.json"
                with open(sample_file, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                print(f"  Sample data saved to: {sample_file}")
                
                # Analyze structure
                if isinstance(data, list) and data:
                    sample_record = data[0]
                    print(f"  Full sample record structure:")
                    for key, value in sample_record.items():
                        value_type = type(value).__name__
                        value_preview = str(value)[:50] if value else "None"
                        print(f"    {key}: {value_type} = {value_preview}")
    else:
        print("✗ No working v1 endpoints found")
        print("💡 v1 API might not be available or have different structure")


if __name__ == "__main__":
    main()
