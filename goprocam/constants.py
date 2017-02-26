start="1"
stop="0"
on="1"
off="0"

class Status:
	Status="status"
	Settings="settings"
	class STATUS:
		Battery="1"
		BatteryLevel="2"
		IsBatteryBacPac="3"
		BatteryBacPacLevel="4"
		QuikCapture="9"
		IsBusy="8"
		Mode="43"
		SubMode="44"
		RecordElapsed="13"
		CamName="30"
		RemVideoTime="35"
		RemPhotos="34"
		BatchPhotosTaken="36"
		VideosTaken="39"
		PhotosTaken="38"
		IsRecording="8"
		RemainingSpace="54"
		TotalHiLights="58"
		LastHiLight="59"
		SdCardInserted="33"
		IsConnected="31"
		GPS="68"
		BattPercent="70"
class Camera:
	Name="model_name"
	Number="model_number"
	Firmware="firmware_version"
	SSID="ap_ssid"
	MacAddress="ap_mac"
	SerialNumber="serial_number"

class Mode:
	VideoMode = "0"
	PhotoMode = "1"
	MultiShotMode = "2"
	class SubMode:
		class Video:
			Video = "0"
			TimeLapseVideo = "1"
			VideoPhoto = "2"
			Looping = "3"
		
		class Photo:
			Single = "0"
			Continuous = "1"
			Night = "2"
		
		class MultiShot:
			Burst = "0"
			TimeLapse = "1"
			NightLapse = "2"

class Shutter:
	ON = "1"
	OFF = "0"


class Delete:
	ALL = "all"
	LAST = "last"

class Locate:
	Start = "1"
	Stop = "0"

class Reset:
	VideoPT="video"
	PhotoPT="photo"
	MultiShotPT="multishot"
	CamReset="camera"


class Setup:
	ORIENTATION="52"
	class Orientation:
		Up="1"
		Down="2"
		Auto="0"
	
	QUIK_CAPTURE="54"
	class QuikCapture:
		ON="1"
		OFF="2"
	
	LED_BLINK="55"
	class LedBlink:
		Led_OFF="0"
		Led_2="1"
		Led_4="2"
	
	LED_BLINK_H5="92"
	class LedBlinkH5:
		Led_OFF="0"
		Led_ON="2"
		Led_FrontOff="1"
	
	BEEP="56"
	class Beep:
		OFF="2"
		SemiLoud="1"
		Loud="0"
	
	AUTO_OFF="59"
	class AutoOff:
		Never="0"
		A1Min="1"
		A2Min="2"
		A3Min="3"
	
	GPS="83"
	class MapLocate:
		ON="1"
		OFF="0"
	
	VOICE_CONTROL="86"
	class VoiceControl:
		ON="1"
		OFF="0"
	
	WIFI="63"
	class Wifi:
		Remote="2"
		SmartRemote="3"
		OFF="0"
	

class Video:
	RESOLUTION="2"
	class Resolution:
		R4k="1"
		R4kSV="2"
		R2k="4"
		R2kSV="5"
		R2k4by3="6"
		R1440p="7"
		R1080pSV="8"
		R1080p="9"
		R960p="10"
		R720pSV="11"
		R720p="12"
		R480p="13"
	
	FRAME_RATE="3"
	class FrameRate:
		FR240="0"
		FR120="1"
		FR100="2"
		FR60="5"
		FR50="6"
		FR48="7"
		FR30="8"
		FR25="9"
		FR24="10"
	
	FOV="4"
	class Fov:
		Wide="0"
		Medium="1"
		Narrow="2"
		SuperView="3"
		Linear="4"
	
	
	LOW_LIGHT="5"
	class LowLight:
		ON="1"
		OFF="0"
	
	SPOT_METER="9"
	class SpotMeter:
		ON="1"
		OFF="0"
	
	VIDEO_LOOP_TIME="6"
	class VideoLoopTime:
		LoopMax="0"
		Loop5Min="1"
		Loop20Min="2"
		Loop60Min="3"
		Loop120Min="4"
	
	VIDEO_PHOTO_INTERVAL="7"
	class VideoPhotoInterval:
		Interval5Min="1"
		Interval10Min="2"
		Interval30Min="3"
		Interval60Min="4"
	
	VIDEO_EIS="78"
	class VideoEIS:
		ON="1"
		OFF="0"
	
	PROTUNE_AUDIO="79"
	class ProtuneAudio:
		ON="1"
		OFF="0"
	
	AUDIO_MODE="80"
	class AudioMode:
		Stereo="0"
		Wind="1"
		Auto="2"
	
	PROTUNE_VIDEO="10"
	class ProTune:
		ON="1"
		OFF="0"
	
	WHITE_BALANCE="11"
	class WhiteBalance:
		WBAuto="0"
		WB3000k="1"
		WB4000k="5"
		WB4800k="6"
		WB5500k="2"
		WB6000k="7"
		WB6500k="3"
		WBNative="4"
	
	COLOR="12"
	class Color:
		GOPRO="0"
		Flat="1"
	
	ISO_LIMIT="13"
	class IsoLimit:
		ISO6400= "0"
		ISO1600= "1"
		ISO400= "2"
		ISO3200= "3"
		ISO800= "4"
		ISO200= "7"
		ISO100= "8"
	
	ISO_MODE="74"
	class IsoMode:
		Max="0"
		Lock="1"
	
	SHARPNESS="14"
	class Sharpness:
		High="0"
		Med="1"
		Low="2"
	
	EVCOMP="15"
	class EvComp:
		P2= "0"
		P1_5="1"
		P1= "2"
		P0_5="3"
		Zero = "4"
		M0_5="5"
		M1= "6"
		M1_5="7"
		M2= "8"

class Photo:
	RESOLUTION="17"
	class Resolution:
		R12W="0"
		R7W="1"
		R7M="2"
		R5W="3"
		#HERO5 black only
		R12L="10"
		R12M="8"
		R12N="9"
	
	SPOT_METER="20"
	class SpotMeter:
		ON="1"
		OFF="0"
	
	NIGHT_PHOTO_EXP="19"
	class NightPhotoExp:
		ExpAuto="0"
		Exp2Sec="1"
		Exp5Sec="2"
		Exp10Sec="3"
		Exp15Sec="4"
		Exp20Sec="5"
		Exp30Sec="6"
	
	CONTINUOUS_PHOTO_RATE="18"
	class ContinuousPhotoRate:
		P3="0"
		P5="1"
		P10="2"
	
	WDR_PHOTO="77"
	class WDR:
		ON="1"
		OFF="0"
	
	RAW_PHOTO="82"
	class RawPhoto:
		ON="1"
		OFF="0"
	
	PROTUNE_PHOTO="21"
	class ProTune:
		ON="1"
		OFF="0"
	
	WHITE_BALANCE="22"
	class WhiteBalance:
		WBAuto="0"
		WB3000k="1"
		WB4000k="5"
		WB4800k="6"
		WB5500k="2"
		WB6000k="7"
		WB6500k="3"
		WBNative="4"
  
	COLOR="23"
	class Color:
		GOPRO="0"
		Flat="1"
  
	ISO_LIMIT="24"
	class IsoLimit:
		ISO800="0"
		ISO400="1"
		ISO200="2"
		ISO100="3"
	
	ISO_MIN="75"
	class IsoMin:
		ISO800="0"
		ISO400="1"
		ISO200="2"
		ISO100="3"
	
	SHARPNESS="25"
	class Sharpness:
		High="0"
		Med="1"
		Low="2"
  
	EVCOMP="26"
	class EvComp:
		P2= "0"
		P1_5="1"
		P1= "2"
		P0_5="3"
		Zero = "4"
		M0_5="5"
		M1= "6"
		M1_5="7"
		M2= "8"
	


class Multishot:
	RESOLUTION="28"
	class Resolution:
		R12W="0"
		R7W="1"
		R7M="2"
		R5W="3"
		#HERO5 black only
		R12L="10"
		R12M="8"
		R12N="9"
	

	SPOT_METER="33"
	class SpotMeter:
		ON="1"
		OFF="0"
	

	NIGHT_LAPSE_EXP="31"
	class NightLapseExp:
		ExpAuto="0"
		Exp2Sec="1"
		Exp5Sec="2"
		Exp10Sec="3"
		Exp15Sec="4"
		Exp20Sec="5"
		Exp30Sec="6"
	
	NIGHT_LAPSE_INTERVAL="32"
	class NightLapseInterval:
		IContinuous="0"
		I4s="4"
		I5s="5"
		I10s="10"
		I15s="15"
		I20s="20"
		I30s="30"
		I1m="60"
		I2m="120"
		I5m="300"
		I30m="1800"
		I60m="3600"
	
	TIMELAPSE_INTERVAL="30"
	class TimeLapseInterval:
		IHalf1="0"
		I1="1"
		I2="2"
		I5="5"
		I10="10"
		I30="30"
		I60="60"
	
	BURST_RATE="29"
	class BurstRate:
		B3_1="0"
		B5_1="1"
		B10_1="2"
		B10_2="3"
		B10_3="4"
		B30_1="5"
		B30_2="6"
		B30_3="7"
		B30_6="8"
	
	PROTUNE_MULTISHOT="21"
	class ProTune:
		ON="1"
		OFF="0"
	
	WHITE_BALANCE="35"
	class WhiteBalance:
		WBAuto="0"
		WB3000k="1"
		WB4000k="5"
		WB4800k="6"
		WB5500k="2"
		WB6000k="7"
		WB6500k="3"
		WBNative="4"
  
	COLOR="36"
	class Color:
		GOPRO="0"
		Flat="1"
  
	ISO_LIMIT="37"
	class IsoLimit:
		ISO800="0"
		ISO400="1"
		ISO200="2"
		ISO100="3"
	
	ISO_MIN="76"
	class IsoMin:
		ISO800="0"
		ISO400="1"
		ISO200="2"
		ISO100="3"
	
	SHARPNESS="38"
	class Sharpness:
		High="0"
		Med="1"
		Low="2"
  
	EVCOMP="39"
	class EvComp:
		P2= "0"
		P1_5="1"
		P1= "2"
		P0_5="3"
		Zero = "4"
		M0_5="5"
		M1= "6"
		M1_5="7"
		M2= "8"
	

class Livestream:
	RESTART = "restart"
	START = "start"
	STOP = "stop"

class Hero3Commands:
	MODE="CM"
	class Mode:
		VideoMode="01"
		PhotoMode="02"
		BurstMode="03"
		PlayBackMode="05"
	class CaptureSettings:
		ORIENTATION="UP"
		class Orientation:
			UP="00"
			DOWN="01"
		SPOT_METER="EX"
		class SpotMeter:
			ON="01"
			OFF="00"
		VIDEO_PHOTO_INTERVAL="PN"
		class VideoPhotoInterval:
			PNOFF="00"
			PN5Sec="01"
			PN10Sec="02"
			PN30Sec="03"
			PN1Min="04"
		LOOPING_VIDEO="LO"
		class LoopingVideo:
			LOOFF="00"
			LO5Min="01"
			LO20Min="02"
			LO60Min="03"
			LOMAX="05"
		PROTUNE="PT"
		class ProTune:
			ON="1"
			OFF="0"
		#The following settings are for HERO3 Black/HERO3+ Black only.
		WHITE_BALANCE="WB"
		class WhiteBalance:
			WBAuto="00"
			WB3000k="01"
			WB5500k="02"
			WB6500k="03"
			WBRaw="04"
		#The following settings are for HERO3+ Black only.
		COLOR_PROFILE="CO"
		class ColorProfile:
			GoPro="00"
			Flat="01"
		ISO="GA"
		class Iso:
			ISO6400="00"
			ISO1600="01"
			ISO400="02"
		SHARPNESS="SP"
		class Sharpness:
			High="00"
			Med="01"
			Low="02"
		EXPOSURE_COMP="EV"
		class EvComp:
			M2="06"
			M1_5="07"
			M1="08"
			M0_5="09"
			Zero="10"
			P0_5="11"
			P1="12"
			P1_5="13"
			P2="14"
	class Setup:
		DEFAULT_MODE="DM"
		class DefMode:
			Video="00"
			Photo="01"
			Burst="02"
			TimeLapse="03"
		ONE_BTN_MODE="OB"
		class OneButtonMode:
			ON="1"
			OFF="0"
		NTSC="VM"
		class NTSC:
			ON="0"
			OFF="1"
		ON_SCREEN_DISP="OS"
		class OnScreenDisplay:
			ON="1"
			OFF="0"
		LED="LB"
		class StatusLight:
			OFF="00"
			ON_2="01"
			ON_4="02"
		BEEP="BS"
		class Beep:
			OFF="00"
			SemiLoud="01"
			Loud="02"
			
	VIDEO_RESOLUTION="VV"
	class VideoResolution:
		V4k="06"
		V4K_Widescreen="08"
		V2kCin="07"
		V2_7k="05"
		V1440p="04"
		V1080p="03"
		V960p="02"
		V720p="01"
		V480p="00"
	FRAME_RATE="FS"
	class FrameRate:
		FPS12="00"
		FPS15="01"
		FPS24="02"
		FPS25="03"
		FPS30="04"
		FPS48="05"
		FPS50="06"
		FPS60="07"
		FPS100="08"
		FPS120="09"
		FPS240="0a"
	FOV="FV"
	class FOV:
		Wide="00"
		Med="01"
		Narrow="02"
	
	
	PHOTO_RESOLUTION="PR"
	class PhotoResolution:
		PR11MP_W="00"
		PR8MP_M="01"
		PR5MP_W="02"
		PR5MP_M="03"
		PR12MP_W="05"
		PR7MP_W="04"
		PR7MP_M="06"
	CONTINOUOUS_RATE="CS"
	class ContRate:
		Single="00"
		CS3SPS="03"
		CS5SPS="05"
		CS10SPS="0a"
	BURST_RATE="BU"
	class BurstRate:
		BU3_1="00"
		BU10_1="02"
		BU10_2="03"
		BU30_1="04"
		BU30_2="05"
		BU30_3="06"
	TIMELAPSE_RATE="TI"
	class TimeLapseRate:
		TIHalfSecond="00"
		TI1Sec="01"
		TI5Sec="05"
		TI10Sec="0a"
		TI30Sec="1e"
		TI1Min="3c"