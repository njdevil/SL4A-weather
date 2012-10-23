import android
import time

droid = android.Android() 
droid.startLocating()
#sometimes it takes a while to pull the location from the cell network, especially in 2G areas!
time.sleep(15)
data=droid.readLocation().result
try:
    data=data["gps"]
except:
    data=data["network"] 
x=str(data["latitude"])
y=str(data["longitude"])

droid.webViewShow('http://www.wunderground.com/cgi-bin/findweather/getForecast?query='+x+','+y+'&MR=1')

droid.stopLocating()
