import pyaudio  
import wave  
    
chunk = 1024  

print("welcome to the sola command line audio player! this supports: .wav")
file = input("full file location: ")
f = wave.open(file)
#instantiate PyAudio  
p = pyaudio.PyAudio()  

stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
 
data = f.readframes(chunk)  
   
while data:  
    stream.write(data)  
    data = f.readframes(chunk)  

stream.stop_stream()  
stream.close()  
