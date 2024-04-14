import cv2,torch,os,serial,time
from ultralytics import YOLO


cam = cv2.VideoCapture(1) # Utilizar 0 para capturar a Webcam

device = torch.device("cuda" if torch.cuda.is_available() else "cpu") #Detectar se vai utilizar cpu ou gpu 

#model = YOLO("yolov8n.pt")  # carregar modelo inicial 
model = YOLO("best.pt")  # modelo treinado a ser usado
try:
    Arduino = True
    porta_serial = serial.Serial('COM3', 9600) # Caso seja necessario mudar a porta serial 
except:
    Arduino = False
    

print("-"*20)

if torch.cuda.is_available():
    print("Estou usando a GPU")
else:
    print("Estou usando a CPU")
    
if Arduino == True:
    print("Arduino Conectado")
else:
    print("Arduino não Conectado")
print("-"*20)

if cam.isOpened():

    class_obj = ['Reciclavel']

    validacao, frame = cam.read()
  
    while validacao:
        validacao, frame = cam.read()   
        #Ajuste CAM
        #frame = cv2.flip(frame, 1) # Inverter Camera na Horizontal
        frame = cv2.resize(frame, (800, 600)) # Define o tamanho do frame de imagem

        #cv2.imwrite("FotoFinal.png", frame) #Captura a visualização do frame 
        #results = model.predict(conf=0.7,source="FotoFinal.png",verbose=False,stream=True)
        
        results = model(frame,verbose=False,conf=0.85)  # Taxa de confiança minima para demarcar o objeto

        
        

        for result in results:
            boxes = result.boxes  # Caixas delimitadoras das detecções
            cls = result.boxes.cls  # Classe predita para cada detecção
            conf = result.boxes.conf  # Confiança da predição para cada detecção
            # Iterar sobre cada detecção
            for box, pred_cls, pred_conf in zip(boxes, cls, conf):
                # Capturar os valores de xyxy
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                confiabilidade_item = (f'{float(pred_conf.item()):1.4f}')
                cv2.putText(frame, f"{class_obj[int(pred_cls.item())]} - {confiabilidade_item}", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                #print(class_obj[int(pred_cls.item())])
                if class_obj[int(pred_cls.item())] in class_obj:
                    if Arduino == True:
                        porta_serial.write(b'A') #Caso o arduino esteja conectado , envia o comando A na porta Serial
                            
              
                
        cv2.imshow("Capturar Objeto", frame)
       
        key = cv2.waitKey(5)
        if key == 27 or cv2.getWindowProperty("Capturar Objeto", cv2.WND_PROP_VISIBLE) < 1:
            break
        

cam.release()
try:
    porta_serial.close()
except:
    pass

cv2.destroyAllWindows()