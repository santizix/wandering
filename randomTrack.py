from turtle import distance, title
from typing import final
from wandering import ComunWandering, Wandering
from track import Track
from location import Location

from bokeh.plotting import figure, output_file, show

def know_type_wandering(type_wandering):
    if type_wandering.__name__=="comunWandering":
        return "Herrante Comun"
    elif type_wandering.__name__=="RightWandering":
        return "Herrante Derechista"
    else:
        return "Herrante Izquierdista"

def walking(wandering, steps,  type_wandering):
    beginning = [wandering.posicion()]
    
    x_graph = [0]
    y_graph = [0]
    
    for _ in range(steps-1):
        wandering.walk()
        x, y = wandering.posicion()
        x_graph.append(x)
        y_graph.append(y)
       
    know_type = know_type_wandering(type_wandering) 
    graph_steps(x_graph, y_graph, know_type, steps)
    return wandering.distance_origin()
         
    

def simulate_walk(steps, number_attemps,  type_wandering):
    wandering = []
    distances = []
    
    for i in range(number_attemps):
        wandering.append(type_wandering(name =f'kike{i}'))
        simulations_walk = walking(wandering[i], steps, type_wandering)
        distances.append(round(simulations_walk, 1))
    return distances

def graph_steps(x_graph, y_graph, type_wandering, steps):
    graphics = figure(title=type_wandering, x_axis_label='Pasos', y_axis_label='distancia')
    graphics.line(x_graph, y_graph, legend_label=str(steps)+'pasos')
    final_x = x_graph[-1]
    final_y = y_graph[-1]
    graphics.diamond_cross(0, 0, fill_color ="green", line_color ="green", size = 18)
    graphics.diamond_cross(final_x, final_y, fill_color ="red", line_color ="green", size = 18)
    straight_finaly_x = [0, final_x]
    straight_finaly_y = [0, final_y]
    graphics.line(straight_finaly_x, straight_finaly_y, line_width = 2, color="red")
    show(graphics)
 
def main(distances_walk, number_attemps, type_wandering):
 
    
    for steps in distances_walk:
        distances = simulate_walk(steps, number_attemps, type_wandering)
        middle_distance = round(sum(distances) / len(distances), 4)
        max_distances = max(distances)
        min_distances = min(distances)
        print(f'{type_wandering.__name__} Caminata aleatoria de {steps} pasos')
        print(f'Media = {middle_distance}')
        print(f'Max ={max_distances}')
        print(f'Min = {min_distances}')


if __name__ == '__main__':
    
    distances_walk = [1000]
    number_attemps = 1
    main(distances_walk,number_attemps, ComunWandering)
    
               
