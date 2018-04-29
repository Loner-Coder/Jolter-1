<p align="middle"><img src='https://i.imgur.com/lkgCwjI.png' /></p>  

# Jolter
Jolter is a advanced multithreaded Network Stress and Denial of Service Audit Toolkit. A testing suite made for analyzing the strength of your website against different kinds of denial of service attacks.

#### Overview:
Jolter consists of 3 modules presently:

- **HTTP Flood** :- HTTP Flood is a type of Denial of Service attack in which the attacker manipulates HTTP and POST unwanted requests in order to attack a web server or application. In this HTTP flood, several post and get requests are submitted to the website in form of strings. The aim of the attack is when to compel the server to allocate as many resources as possible to serving the attack thus denying legitimate users access to the server's resources. This is a Layer 7 attack tool and can bring down unpatched, misconfigured webservers within seconds.

- **TCP SYN Flood** :- A SYN flood is a form of denial-of-service attack in which an attacker sends a succession of SYN requests to a target's system in an attempt to accomplish as many as 3 way SYN-ACK handshakes, pretending to be no. of different users trying to connect with the website. This consumes enough server resources to make the system unresponsive to legitimate traffic. This modules camouflages the final IPs of the SYN-ACK handshakes, thereby providing more effectiveness.

- **UDP Flood** :- A UDP flood attack is a denial-of-service (DoS) attack using the User Datagram Protocol (UDP), a sessionless/connectionless computer networking protocol. This method sends huge volumes of data packets on random ports thus hitting the website very seriously.

#### Features:

- [x] Includes 3 major modules commonly used in DoS attacks.
- [x] Everything is multithreaded for high effectiveness.
- [x] Includes a Layer 7 DoS, SYN Flooder, and UDP Flooder.
- [x] Has a user-friendly interaction environment.
- [x] Spoofs requests with random IPs to prevent exposure.

#### Requirements:

- scapy
- urllib2
- requests
- socket
- logging

#### Usage:

- Clone the script and launch it.
```
git clone https://github.com/code-sploit/Jolter.git
cd Jolter
```
- Install the dependencies.
```
pip install -r requirements
```
- Launch the script.
```
python jolter.py
```
- Enter the website target.
- Choose your flood attck vector.
- Watch your victim crumble down to knees. ; )

#### Version:

- v1.1.0

#### To Do's:
- Include more flood attck vectors like Amplification attacks.

> Thank you...
 ✎ Team CodeSploit
