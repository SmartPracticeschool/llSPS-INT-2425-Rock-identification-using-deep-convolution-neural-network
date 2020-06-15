import numpy as np
import os
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf

global graph
graph = tf.get_default_graph() #to see the predictions it is required without this it willnot work

from flask import Flask , request, render_template,url_for
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
model = load_model("RockIdentification.h5")

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/predict',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        
        #saving the image in uploads folder
        print("current path")
        basepath = os.path.dirname(__file__)
        print("current path", basepath)
        filepath = os.path.join(basepath,'static',f.filename)
        print("upload folder is ", filepath)
        f.save(filepath)
        
        #CNN part
        img = image.load_img(filepath,target_size = (64,64))
        x = image.img_to_array(img)
        x = np.expand_dims(x,axis =0)
        
        with graph.as_default():
            preds = model.predict_classes(x)
            
            
            print("prediction",preds)
        index =['Basalt', 'Conglomerate', 'Dolostone', 'Gabbro', 'Gneiss', 'Granite', 'Limestone', 'Marble', 'Quartzite', 'Rhyolite', 'Sandstone', 'Shale', 'Slate']
        rock=str(index[preds[0]])
    if rock=="Gabbro":
        rocktype="Igneous (intrusive/plutonic)"
        comp="feldspar, olivine, pyroxene, amphibole"
        env="Gabbro is formed by magma that cools very slowly into hard rock below or within the Earth’s crust.Often chromium, nickel and platinum occur in association with Gabbro."
        char="dark grey-black, shiny surfaces of feldspar are visible."
        use="Gabbro is too fragile to use in construction."
        
    elif rock=="Basalt":
        rocktype="Igneous (extrusive/volcanic)"
        comp="feldspar, olivine, pyroxene, amphibole"
        env="Basalt is solidified lava, like rhyolite. However, it flows much quicker because it is less viscous. The Hawaiian Islands are made of basaltic lava. The ocean floor is also mostly basalt."
        char="red-brown to black, frothy with small visible holes where gas escaped while the lava cooled."
        use="Basalt is crushed and used as crushed stone, concrete aggregate and railroad ballast. Basalt fibres are used in the production of high quality textile fibres, floor tiles, basalt plastic reinforcement bars, basalt fibre roofing felt and glass wool (fibre glass)."
        
        
    elif rock=="Conglomerate":
        rocktype="Sedimentary"
        comp="fragments of other rocks and minerals cemented by silica, calcite, or iron oxide."
        env="The rock fragments can be rounded from being rolled along a stream bed or a beach during transportation. If the fragments embedded in the matrix are angular instead of rounded, the rock is called a breccia (pronounced BRECH-i-a)."
        char="dark grey with imbedded fragments"
        use="conglomerate is used in the construction industry"
        
                
    elif rock=="Dolostone":
        rocktype="Sedimentary"
        comp="dolomite and fossils"
        env="Sea water, high in magnesium, flows through porous limestone and replaces some of the calcium with magnesium turning limestone into dolostone. Fossils are plants or animals that have been preserved in rock as organic carbon, chitin, or some mineral that replaced the original tissue. When an animal or plant dies its body can end up being buried by mud or other sediments. The hard parts (skeleton, teeth, shell) and sometimes tissue (leaves, flowers, muscle, cartilage) may be preserved when the sediments become rock."
        char="Grey with fossils that are visible. Anything that looks like it was once alive may be a fossil. Fossils are often the same colour as the rocks in which they are found."
        use="Dolostone from the Niagara Escarpment is used as high quality construction aggregates. It is found in asphalt mixes for roads and streets, high strength concrete mixes used for high-rise residential buildings, bridge overpasses, sidewalks and airport runways. Crushed dolostone is used to create drainage layers under high volume roads and is found in uncontaminated construction fill."
        
         
          
        
    elif rock=="Gneiss":
        rocktype="Metamorphic"
        comp="quartz, feldspar, mica"
        env="Gneiss forms at high temperatures and pressures. The temperature needed is about 700°C and the pressure needs to be about 12-15 kilo bars, which is at a depth of about 40 km!"
        char="banded with alternating layers of dark and light minerals."
        use="Gneiss is used in construction, aggregate and for ornamental  purposes."
        
        
    
        
        
        
    elif rock=="Granite":
        rocktype="Igneous (intrusive/plutonic)"
        comp="feldspar, quartz, mica, hornblend"
        env="Granite is formed by magma that cools very slowly into hard rock below or within the Earth’s crust."
        char="Visible crystals of pink feldspar, white or grey quartz, and black mica. There is no horizontal banding in granite."
        use="Granite is used for kitchen countertops and as a decorative building material. Granite is not fire-safe because it can crack in high heat"
          
        
        
        
        
    elif rock=="Limestone":
        rocktype="Sedimentary"
        comp="mostly calcite"
        env="There are several ways for limestone to form. Calcite dissolves easily in warm water but when the concentration reaches a certain threshold, the calcite comes out of solution and is deposited on the sea floor as a chemical precipitate. The precipitates can build up along with other sediments or on their own and eventually form limestone. Another way for limestone to form is by the build up of the shells and skeletons of marine animals."
        char="whitish-grey with a chalky texture. There are no visible fossils in these samples."
        use="This highly pure limestone is used as flux in the steel making process and is used in the production of glass. Other applications include paper production, sugar refining, acid lake treatment and flue gas desulphurisation. Limestone has construction, agricultural and automotive applications. It is also supplied to feed mills and chicken farmers. "
        
      
    elif rock=="Marble":
        rocktype="Metamorphic"
        comp="very pure, recrystallized calcite"
        env="Marble forms at many temperatures and pressures."
        char="medium to coarser grained, light coloured and calcite crystals may be visible. Holing these samples up to the light and slowly turning them will reveal a slight sparkle."
        use="Marble is used for construction, countertops, and carvings, and may be a source for magnesium. "
        
        
        

        
        
        
        
        
        
    elif rock=="Quartzite":
        rocktype="Metamorphic"
        comp="recrystallized quartz grains"
        env="Quartzite forms at many temperatures and pressures."
        char="light grey or white, medium grained, very hard."
        use="Quartzite is the raw material for the glass and ceramics industries."
        
        
        
        

        
        
        
    elif rock=="Rhyolite":
        rocktype="Igneous (extrusive/volcanic)"
        comp="feldspar, quartz, mica, hornblend"
        env="Rhyolite is formed by magma that has reached the Earth’s surface (lava) and therefore cools very quickly. Lava can explode out of a volcano and make pumice or ash, or flow down its side and make thick layers of fine grained rock or volcanic glass."
        char="Very fine grained, pinkish-grey, sometimes with dark streaks. If dipped in water and rubbed on a piece of paper, rhyolite will likely tear the paper rather than leave a muddy streak."
        use="Black volcanic glass called obsidian and frothy-looking white coloured rock called pumice are other forms of rhyolite. Pumice is used in abrasives, concrete, stone-washing laundries, hand soap, emery boards, and sandpaper and is used in sandblasting"
        
        
  
        
        
        
    elif rock=="Sandstone":
        rocktype="Sedimentary"
        comp=" grains of sand that can be feldspar or quartz - the amount of other minerals, such as mica, depend on how much weathering has occurred."
        env="Already existing rocks are eroded and the grains are transported and sorted by rivers. The resulting sand is deposited on beaches, along floodplains or in deltas, where it is eventually buried by other sediments. This causes a slow squeezing of the sediments. As the sediments are compacted, fine clay helps to fuse the larger particles together. The sediments are also cemented by chemicals left by the water in the original sediment. The presence of sandstone indicates that there was water with fairly high energy (waves on a beach or a fast moving river)"
        char="Coarse to very fine grains, beige to grey colour, feels like sandpaper."
        use="Sandstone is used for flagstone to line your walkway or patio. It is also an important building stone. "
        
        
        
        
    elif rock=="Shale":
        rocktype="Sedimentary"
        comp="grains of clay"
        env="Shale sediments are deposited in still water (low energy) such as a lake or a deep, slow river."
        char=" dull, reddish- brown, very fine grains (smooth to the touch), breaks easily. If an edge is dipped in water and drawn along a surface, shale will leave a muddy streak."
        use="This shale is the raw material for the brick manufacturing industry in Ontario"
        

    
    elif rock=="Slate":
        rocktype="Metamorphic"
        comp="clay minerals"
        env="Slate forms from the heat and pressure when shale is buried deep in the crust. The depth of burial to make slate out of shale is about 10 km. The temperature at that depth is about 200°C."
        char="dark grey to black, very fine grains (smooth to the touch), harder than shale, distinct layers are visible."
        use="slate is used in flooring and roofing materials. In the past, slate was used as chalkboards"
    

        
    
       
    return render_template('base.html',lab0="Report",lab1=rock,lab2=f.filename,lab3=rocktype,lab4=comp,lab5=env,lab6=char,lab7=use,l1="Rock Type   ",l2="Composition ",l3="Environment ",l4="Characterstics ",l5="Use ",l0=" Rock")

if __name__ == '__main__':
    app.run(debug = True, threaded = False)
        
        
        
    
    
    
