import os

directory = "/Users/gudmian/Documents/OCTNet/OCTNet/dataset"

def train_and_test_data():
    data = []
    for filename in os.listdir(directory):
        if "_map" in filename:
            traj_file = filename.replace("_map", "_trajs")
            print("file:{} and trajs:{}".format(filename, traj_file))
            map_data = parse_map(directory + '/' + filename)
            traj_data = parse_traj(directory + '/' + traj_file)
            print(len(traj_data))
            data.append((map_data, traj_data))

    split_index = len(data) - int(len(data) * 0.2)
    print("Data - size:{}, split{}".format(len(data), split_index))
    (m, t) = data[0]
    print("Traj: {}".format(t[0]))
    print("Map: {}".format(m))
    return (data[:split_index], data[split_index:])

def parse_map(path):
    map = []
    with open(path) as f:
        for line in f:
            for c in line:
                if c in "[]":
                    line = line.replace(c,'')
            mapline = [int(x) for x in line.split()] 
            map.append(mapline)
    return map

def parse_traj(path):
    trajs = []
    with open(path) as f:
        for line in f:
            if not line.startswith("traj"):
                waypoints = [float(x) for x in line.split()] 
                trajs.append(waypoints)
    return trajs
           

if __name__ == "__main__":
    train_and_test_data()