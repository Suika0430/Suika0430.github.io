import glob
import yaml
import os

def main():
    data = []
    for path in glob.glob("assets/img/gallery/*"):
        data.append({"thumbnail": os.path.basename(path)})
        
    with open('_data/gallery.yaml', 'w') as file:
        yaml.dump(data, file)
        

if __name__ == "__main__":
    main()