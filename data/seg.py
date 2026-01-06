import pandas as pd
df = pd.read_csv('top_50_europe_trekking.csv')

df['effort_index'] = (df['elevation_gain'] / df['distance_km']).round(2)

def segment_route(dist):
    if dist < 30: return 'Day Trip'
    if dist < 150: return 'Multi-Day'
    return 'Thru-Hike'

df['category'] = df['distance_km'].apply(segment_route)

df.to_csv('segmented_trekking_routes.csv', index=False)