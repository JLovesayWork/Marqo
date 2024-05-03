from Models.vehicle import Vehicle
from Scripts.Vehicles.vehicle_search import search_vehicles

def process_vehicle_queries(mq):
    
    vehicles = create_marqo_vehicles()
    create_index(mq)
    add_vehicles_to_index(mq, vehicles)
    search_vehicles(mq)

def create_index(mq):
    complex_settings = {
        "treat_urls_and_pointers_as_images": True,
        "model": "open_clip/ViT-B-32/laion2b_s34b_b79k",
    }

    mq.delete_index("complex-vehicle-index")
    mq.create_index("complex-vehicle-index", **complex_settings)
    
    simple_settings = {
        "treat_urls_and_pointers_as_images": True,
        "model": "hf/e5-base-v2",
    }

    mq.delete_index("simple-vehicle-index")
    mq.create_index("simple-vehicle-index", **simple_settings)
    
    multi_modal_settings = {
        "treat_urls_and_pointers_as_images": True,
        "model": "open_clip/ViT-B-32/laion2b_s34b_b79k",
    }

    mq.delete_index("multimodal-vehicle-index")
    mq.create_index("multimodal-vehicle-index", **multi_modal_settings)
    
def add_vehicles_to_index(mq, vehicles):
    
    result = mq.index("simple-vehicle-index").add_documents(
        vehicles,
        tensor_fields=["Description"]
    )   
    
    result = mq.index("complex-vehicle-index").add_documents(
        vehicles,
        tensor_fields=["description_image"],
        mappings={
            "description_image": {
                "type": "multimodal_combination",
                "weights": {"Description": 1.0, "image": 1.1}
            }
        }
    )    
    
    result = mq.index("multimodal-vehicle-index").add_documents(
        vehicles,
        tensor_fields=["image"],
    )    
    

def create_marqo_vehicles():
    
    # List of vehicles
    vehicles = [
        Vehicle("Toyota", "Corolla", "The Toyota Corolla is a compact car that has been popular for decades due to its reliability and fuel efficiency.", "https://th.bing.com/th/id/OIP.RDRsqyBBWPq7-pFwCB82kAAAAA?rs=1&pid=ImgDetMain"),
        Vehicle("Honda", "Civic", "The Honda Civic is a versatile compact car known for its strong resale value and spacious interior.", "https://th.bing.com/th/id/OIP.fkJ1bomol_N1xA-lKLKCxgAAAA?rs=1&pid=ImgDetMain"),
        Vehicle("Ford", "F-150", "The Ford F-150 is a full-size pickup truck renowned for its towing capacity and rugged durability.", "https://th.bing.com/th/id/OIP.76zhibpUqGvcrLJ_2k7S3AAAAA?rs=1&pid=ImgDetMain"),
        Vehicle("Chevrolet", "Silverado", "The Chevrolet Silverado is a powerful pickup truck known for its range of powerful engines and comfortable ride.", "https://th.bing.com/th/id/OIP.tWdWWscSV_EtD1lOX5-gJAHaEK?rs=1&pid=ImgDetMain"),
        Vehicle("BMW", "3 Series", "The BMW 3 Series is a luxury sedan that offers a blend of performance, comfort, and advanced technology.", "https://i.ebayimg.com/00/s/ODcwWDEwMjQ=/z/yeoAAOSwoWFfajg5/$_86.JPG"),
        Vehicle("Mercedes-Benz", "E-Class", "The Mercedes-Benz E-Class is a midsize luxury sedan known for its refined interior and advanced safety features.", "https://3.bp.blogspot.com/-aqxm0t8Fn7o/VYWqy6CCRZI/AAAAAAAAci4/_sVKlYLuyjw/s1600/Mercedes-Benz-E63-AMG-On-PUR-LX04.V3-By-PUR-Wheels-08.jpg"),
        Vehicle("Tesla", "Model S", "The Tesla Model S is an all-electric luxury sedan with cutting-edge technology and impressive acceleration.", "https://th.bing.com/th/id/OIP.crh79n6-1c_yw-A92OFwmgHaE7?rs=1&pid=ImgDetMain"),
        Vehicle("Jeep", "Wrangler", "The Jeep Wrangler is a rugged SUV known for its off-road capability and iconic design.", "https://i.redd.it/3z40windqz611.jpg"),
        Vehicle("Toyota", "Land Cruiser", "The Toyota Land Cruiser is a legendary off-road SUV known for its durability and exceptional off-road performance.", "https://media.autoexpress.co.uk/image/private/s--RKkEstDN--/v1563184111/autoexpress/2018/02/dsc_8589.jpg"),
        Vehicle("Ford", "Mustang", "The Ford Mustang is an iconic sports car with a powerful engine and timeless design.", "https://th.bing.com/th/id/R.7164615f870e624ef8fddaffa78cd5b7?rik=d0%2feBJ4IUzS46A&pid=ImgRaw&r=0"),
        Vehicle("Chevrolet", "Camaro", "The Chevrolet Camaro is a classic American muscle car known for its performance and aggressive styling.", "https://th.bing.com/th/id/R.845ba976284ed4f3f35cb8b0bff494f8?rik=4G%2bRZjv3MzKBvw&pid=ImgRaw&r=0"),
        Vehicle("Nissan", "Altima", "The Nissan Altima is a reliable midsize sedan known for its comfortable ride and fuel efficiency.", "https://th.bing.com/th/id/OIP.aOn8JmM9yvgc5azH9tjDnwHaEK?rs=1&pid=ImgDetMain"),
        Vehicle("Honda", "Accord", "The Honda Accord is a popular midsize sedan known for its spacious interior and strong resale value.", "https://th.bing.com/th/id/OIP.7z-It3G_8n6sJZU9wwjlSAHaFj?rs=1&pid=ImgDetMain"),
        Vehicle("Toyota", "Rav4", "The Toyota RAV4 is a compact SUV known for its practicality, reliability, and fuel efficiency.", "https://th.bing.com/th/id/OIP.oW4oWDKk0Dp293gWi8xVwgAAAA?rs=1&pid=ImgDetMain"),
        Vehicle("Subaru", "Outback", "The Subaru Outback is a versatile crossover SUV known for its capable all-wheel drive system and spacious cargo area.", "https://th.bing.com/th/id/R.a2d4814d54d6e21ee49ec37b17418dea?rik=X2CfDIthCEh1vQ&riu=http%3a%2f%2fcdn.carbuzz.com%2fgallery-images%2f1600%2f503000%2f600%2f503678.jpg&ehk=eijOR33J55jngFpSClCzgdx7B96%2foYRm4WqQn6eE9B0%3d&risl=&pid=ImgRaw&r=0"),
        Vehicle("Ford", "Explorer", "The Ford Explorer is a midsize SUV known for its spacious interior, strong towing capacity, and advanced safety features.", "https://th.bing.com/th/id/OIP.rarQy7geSKIj-kSrsW-JcAHaE8?rs=1&pid=ImgDetMain"),
        Vehicle("Audi", "A4", "The Audi A4 is a luxury sedan known for its refined interior, smooth ride, and advanced technology features.", "https://th.bing.com/th/id/OIP.TiAkpXmxN0mNstaiuCirpgAAAA?rs=1&pid=ImgDetMain"),
        Vehicle("Tesla", "Model 3", "The Tesla Model 3 is a compact all-electric sedan with impressive range and advanced self-driving capabilities.", "https://cdn.motor1.com/images/mgl/qpGBL/s1/tesla-model-3-gray-2.jpg"),
        Vehicle("Chevrolet", "Tahoe", "The Chevrolet Tahoe is a full-size SUV known for its spacious interior, powerful engine options, and towing capability.", "https://th.bing.com/th/id/R.0e0c49d404451b8ce3ad1137a455859d?rik=7lrQBPBuLjvpHg&riu=http%3a%2f%2fgmauthority.com%2fblog%2fwp-content%2fuploads%2f2019%2f11%2f1999-Chevrolet-Tahoe-001.jpg&ehk=DmYUz2jZa8tjDidZtCdbwHUSstpVcIzYq8Dp813CKk8%3d&risl=&pid=ImgRaw&r=0"),
        Vehicle("GMC", "Sierra", "The GMC Sierra is a rugged full-size pickup truck known for its powerful engine options and luxurious interior.", "https://th.bing.com/th/id/OIP.FevLpzD0FYeENehOBl_x6AAAAA?rs=1&pid=ImgDetMain")
    ]

    # Convert vehicles to Marqo documents
    marqo_documents = [vehicle.to_marqo_document() for vehicle in vehicles]   
    
    return marqo_documents