# Touch Grass

## Description
Hackers never touch grass. So for public good, I have made a Pedometer app that counts steps and gives flag after you walk 15k steps. So get up from your chairs and start running.

PS: The app uses phone's accelerometer to track steps. If the app does not work try reinstalling it without scanning for viruses and allow required permissions.

## Solution [Patching the APK]
Use apktool to decode the given APK file.
```
apktool d PedoApp.apk
```
After decoding the apk and exploring `smali/io/flutter/plugins/` directory, we know that the apk uses `pedometer` and `sensor_plus` plugins to perform step counting. After reading the plugin docs, unfortunately i didn't get anything i could patch. Then a found something useful in this [doc](https://developer.android.com/reference/android/hardware/SensorEventListener#onSensorChanged(android.hardware.SensorEvent)). From the doc we get something interesting.

```
onSensorChanged
Added in API level 3

public abstract void onSensorChanged (SensorEvent event)
Called when there is a new sensor event. Note that "on changed" is somewhat of a misnomer, as this will also be called if we have a new reading from a sensor with the exact same sensor values (but a newer timestamp). 

See SensorManager for details on possible sensor types.

See also SensorEvent.

NOTE: The application doesn't own the event object passed as a parameter and therefore cannot hold on to it. The object may be part of an internal pool and may be reused by the framework.

Parameters
event	SensorEvent: the SensorEvent.
```
Where the `event` object has a `values` field.     
```
values
Added in API level 3

public final float[] values
The length and contents of the values array depends on which sensor type is being monitored (see also SensorEvent for a definition of the coordinate system used).
```
Then i use 
```
grep -ra "onSensorChanged"
```
to search where that public method is writte. It turns out the public method is written in `smali/m/b$a.smali`. We can read read the decompiled version on `sources/m/b.java`.

```java
@Override // android.hardware.SensorEventListener
public void onSensorChanged(SensorEvent event) {
    i.e(event, "event");
    this.f1103a.b(Integer.valueOf((int) event.values[0]));
}
```
Because the goal of this challenge is to do 15k steps. So i multiply the value of `event.values[0]` by 1000. So we only need to do 15 steps. Modify the `smali/m/b$a.smali` onSensorChanged method to.

```smali
.method public onSensorChanged(Landroid/hardware/SensorEvent;)V
    .locals 1

    const-string v0, "event"

    invoke-static {p1, v0}, Lkotlin/jvm/internal/i;->e(Ljava/lang/Object;Ljava/lang/String;)V

    iget-object p1, p1, Landroid/hardware/SensorEvent;->values:[F

    const/4 v0, 0x0

    aget p1, p1, v0
	
    float-to-int p1, p1
	
	mul-int/lit16 p1, p1, 0x3E8
	
    iget-object v0, p0, Lm/b$a;->a:La0/d$b;

    invoke-static {p1}, Ljava/lang/Integer;->valueOf(I)Ljava/lang/Integer;

    move-result-object p1

    invoke-interface {v0, p1}, La0/d$b;->b(Ljava/lang/Object;)V

    return-void
```
I only add this line `mul-int/lit16 p1, p1, 0x3E8`.

After that rebuild the apk using this command.
```
apktool b PedoApp
```
Then sign the apk using [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer).
```
java -jar uber-apk-signer-1.3.0.jar --apks PedoApp/dist
```
Install the APK then do 15 steps.

Note : if you get error when installing the apk, use
```
apktool d PedoApp.apk --no-res
```
instead of above command.