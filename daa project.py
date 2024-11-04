import tkinter as tk
import sys

cities = ["Delhi", "Mumbai", "Bengaluru", "Hyderabad", "Chennai", "Kolkata"]
distances = [
    [0, 1450, 0, 900, 0, 1720],  
    [1050, 0, 1500, 1750, 0, 0],  
    [0, 2000, 0, 600, 500, 0],  
    [0, 1750, 600, 0, 350, 0],  
    [0, 0, 500, 350, 0, 660],  
    [1720, 0, 0, 500, 660, 0]    
]

def dijkstra(start, end): 
    num_cities = len(cities)
    dist = [sys.maxsize] * num_cities
    dist[start] = 0
    visited = [False] * num_cities
    prev = [None] * num_cities

    for _ in range(num_cities):
        u = None
        min_distance = sys.maxsize

        for i in range(num_cities):
            if not visited[i] and dist[i] < min_distance:
                min_distance = dist[i]
                u = i

        if u is None:
            break
        visited[u] = True

        for v in range(num_cities): 
            if distances[u][v] > 0 and not visited[v]: 
                new_dist = dist[u] + distances[u][v]
                if new_dist < dist[v]: 
                    dist[v] = new_dist
                    prev[v] = u

    path = []
    current_city = end
    while current_city is not None:
        path.append(cities[current_city])
        current_city = prev[current_city]
    path.reverse()

    return dist[end], path 

def calculate(): 
    start = cities.index(start_city_var.get())
    end = cities.index(end_city_var.get())
    distance, path = dijkstra(start, end)
    result_var.set(f"Distance: {distance} km\nRoute: {' -> '.join(path)}")

root = tk.Tk()
root.title("Distance Finder")

start_city_var = tk.StringVar(value=cities[0])
tk.Label(root, text="Start City:").pack()
tk.OptionMenu(root, start_city_var, *cities).pack()

end_city_var = tk.StringVar(value=cities[1])
tk.Label(root, text="End City:").pack()
tk.OptionMenu(root, end_city_var, *cities).pack()

tk.Button(root, text="Find Distance", command=calculate).pack()

result_var = tk.StringVar()
tk.Label(root, textvariable=result_var).pack()

root.mainloop()
