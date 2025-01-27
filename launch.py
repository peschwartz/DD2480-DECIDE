from typing import List

def compute_launch(FUV: List[bool]) -> str:
    return "YES" if all(FUV) else "NO"