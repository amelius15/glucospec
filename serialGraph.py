import serial
import matplotlib.pyplot as plt
import pickle
from twilio.rest import TwilioRestClient

ser = serial.Serial('/dev/cu.usbmodem1451', 115200)
x = range(46)
y = [0.0]*len(x)
# fs = open('savedData.txt' , 'a')
# plt.axis([0, 200, 0, 1024])
# plt.ion()
# plt.show()
store = []
while True:
    try:
        ln = ser.readline()
        data = [float(i) for i in ln.split(':::')]
        y[data[0]]= data[1]
        # plt.scatter(data[0],data[1])
        # if data[0] == 199:
        #     break
        # plt.draw()
        fs = open('data.pickle', 'w')
        p,q = pickle.load(fs)

        fs.write(ln + ':::' + '\n')
    except:
        pass

account_sid = "AC8d1bca20b46706ba7f32bca1f70990ea"
auth_token  = "968c12324d902c4fb8bf71963cbccd6f"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hi Doc! My blood glucose is too high.",
    to="+14159696123",
    from_="+14159666750")
print message.sid
