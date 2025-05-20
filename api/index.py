from http import HTTPStatus
import json
import os
from typing import Dict, List, Optional

data = [
    {"name": "tr", "marks": 31}, {"name": "H0xkeYbb", "marks": 45}, {"name": "wGUW", "marks": 10},
    {"name": "xPFz", "marks": 65}, {"name": "uaJ", "marks": 57}, {"name": "TJrqjigUZW", "marks": 74},
    {"name": "A1b", "marks": 22}, {"name": "SNgJI9", "marks": 21}, {"name": "Jtzv0Gc69", "marks": 10},
    {"name": "GUTI0dGAW", "marks": 36}, {"name": "vMRj9", "marks": 23}, {"name": "3sFXcD74G", "marks": 90},
    {"name": "g", "marks": 40}, {"name": "cmk", "marks": 87}, {"name": "zh", "marks": 55},
    {"name": "aVVqmN", "marks": 8}, {"name": "s3rYeT", "marks": 65}, {"name": "Yqtq", "marks": 43},
    {"name": "CZr6RK", "marks": 72}, {"name": "C4Xu1mAHj", "marks": 28}, {"name": "N", "marks": 40},
    {"name": "yt", "marks": 78}, {"name": "MC15q", "marks": 95}, {"name": "x", "marks": 11},
    {"name": "o", "marks": 84}, {"name": "bWIEzBWTt", "marks": 28}, {"name": "QkjtWinxmg", "marks": 80},
    {"name": "QcR5vpkrb1", "marks": 27}, {"name": "iLIfz", "marks": 35}, {"name": "dfRbjgFFlG", "marks": 23},
    {"name": "l3gJ5VVyg", "marks": 89}, {"name": "u67gofI", "marks": 77}, {"name": "WspyQ", "marks": 89},
    {"name": "ZP7n36", "marks": 96}, {"name": "vLzM", "marks": 58}, {"name": "yUSwq4esTy", "marks": 4},
    {"name": "AI5u", "marks": 32}, {"name": "yqeNzN", "marks": 5}, {"name": "MTeYM", "marks": 12},
    {"name": "36Z2I", "marks": 4}, {"name": "kcsH", "marks": 56}, {"name": "k", "marks": 96},
    {"name": "txt3WWc0o", "marks": 97}, {"name": "sF", "marks": 53}, {"name": "s8ye", "marks": 39},
    {"name": "K", "marks": 19}, {"name": "5auNA", "marks": 52}, {"name": "8mkW", "marks": 72},
    {"name": "Vq", "marks": 85}, {"name": "OR1Bi2Uo", "marks": 39}, {"name": "EKuyo9P", "marks": 71},
    {"name": "HYRGluoKow", "marks": 81}, {"name": "pNuMT9C6Df", "marks": 33}, {"name": "Ei6AXm2", "marks": 77},
    {"name": "9", "marks": 74}, {"name": "btWepwM", "marks": 12}, {"name": "Aaqwg", "marks": 43},
    {"name": "TPkKg", "marks": 75}, {"name": "5b", "marks": 75}, {"name": "TRds", "marks": 88},
    {"name": "N7Ha", "marks": 22}, {"name": "uZB1aYCCm", "marks": 88}, {"name": "gaLVo4Ewv", "marks": 52},
    {"name": "j", "marks": 24}, {"name": "n", "marks": 15}, {"name": "IbZ9y", "marks": 26},
    {"name": "K5t5dvvOK", "marks": 36}, {"name": "evJ", "marks": 15}, {"name": "GCxu1uz", "marks": 46},
    {"name": "C2SWCF", "marks": 78}, {"name": "UABpAZsCV", "marks": 89}, {"name": "RrVahs4", "marks": 35},
    {"name": "LSygC", "marks": 27}, {"name": "tZBvoe", "marks": 71}, {"name": "S", "marks": 31},
    {"name": "p9GISHolcz", "marks": 91}, {"name": "AJnUtFprNQ", "marks": 8}, {"name": "hXw", "marks": 62},
    {"name": "bptQbtw4h", "marks": 76}, {"name": "uC5ftAci", "marks": 14}, {"name": "Ux", "marks": 40},
    {"name": "tzKq4I", "marks": 7}, {"name": "pKrD12", "marks": 97}, {"name": "J", "marks": 53},
    {"name": "ZTva", "marks": 2}, {"name": "Uw", "marks": 56}, {"name": "B9ZFkEz6Zq", "marks": 38},
    {"name": "Wgxmzsiiv", "marks": 59}, {"name": "V", "marks": 86}, {"name": "YzA2VwIRp", "marks": 14},
    {"name": "xnfSjk", "marks": 60}, {"name": "YqcR", "marks": 88}, {"name": "RPhiu", "marks": 54},
    {"name": "i1y2o96Gv", "marks": 77}, {"name": "3EKZA71", "marks": 92}, {"name": "ZGeV", "marks": 19},
    {"name": "qehEXjyTw", "marks": 96}, {"name": "oA58v", "marks": 66}, {"name": "wFV7vXY0", "marks": 65}
]

def find_marks(names: List[str]) -> List[Optional[int]]:
    name_to_marks = {item["name"]: item["marks"] for item in data}
    return [name_to_marks.get(name) for name in names]

def handler(event, context):
    from urllib.parse import parse_qs
    
    # Handle CORS preflight request
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": HTTPStatus.OK,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type",
            },
            "body": "",
        }
    
    # Parse query parameters
    query_params = parse_qs(event.get("queryStringParameters", "") or "")
    names = query_params.get("name", [])
    
    if not names:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
            },
            "body": json.dumps({"error": "No names provided in query parameters"}),
        }
    
    marks = find_marks(names)
    
    response = {
        "statusCode": HTTPStatus.OK,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps({"marks": marks}),
    }
    
    return response
