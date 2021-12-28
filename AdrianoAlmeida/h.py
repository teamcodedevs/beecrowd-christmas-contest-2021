'''input
6 8
danbury norwalk waterbury stamfort bridgeport trenton
danbury stamfort
bridgeport trenton
trenton danbury
waterbury trenton
stamfort norwalk
trenton norwalk
norwalk waterbury
norwalk danbury
'''
n_city, n_routes = list(map(int, input().split()))


region = {city_name for city_name in input().split()} 
src_ = set()
dst_ = set()

for _ in range(n_routes):
	src, dst = input().split()
	src_.add(src)
	dst_.add(dst)

print(f"merry christmas" if len(src_) == len(dst_) and len(src_) == len(region) else "no gifts today")
