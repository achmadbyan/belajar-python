#fungsi mengembalikan beberapa nilai sekaligus 
def statistik(data):
    total = sum(data)
    rata = total / len(data)
    minimum = min(data)
    maksimum = max(data)
    return total, rata, minimum, maksimum
    
nilai = [75, 82, 90, 68, 95]
tot, avg, mn, mx = statistik(nilai)
print(f"Total: {tot} | Rata: {avg} | Min: {mn} | Max: {mx}")