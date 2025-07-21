# BasicNetworkSecurity

This is a set of basic network security tasks!

# Passwords
On this network I will be applying MD5 hash (level 5) encrypted passwords, and scrypt encrypted (level 9) passwords.

<img width="508.2" height="323.4" alt="image" src="https://github.com/user-attachments/assets/5d43886b-8af3-4cea-bc54-faeaa6341ae1" />

<img width="306.6" height="280.7" alt="image" src="https://github.com/user-attachments/assets/cb95c7a4-2aa0-47c9-b9ef-0aa975a81e65" />

Sometimes type 9 passwords or passwords made with the scrypt hash algorithm aren't an option, so you need to use MD5 Hash.
I have one example of each, type 9 scrypt, is the more secure, it is computationally intensive and resistant to brute-force attacks compared to the MD5 algorithm used by Type 5. So whenever given the chance, use type 9.



<img width="562" height="222" alt="image" src="https://github.com/user-attachments/assets/0d90a547-9184-4d73-b0d2-1e48d4c16c0f" />
<img width="643" height="46" alt="image" src="https://github.com/user-attachments/assets/b6683a69-cff9-4bcd-a6f8-a8387731db07" />


# VLANS

On my lab we have quite a few devices, and often for efficiency and security, we want to seperate the traffic through the network into different logical segments using VLANs, 
this way only devices on the 'Management' VLAN, receive traffic meant for management, and so forth. 
<img width="988" height="576" alt="image" src="https://github.com/user-attachments/assets/0d44e74c-4365-4f68-9bb5-939624de279d" />

<img width="656" height="306" alt="image" src="https://github.com/user-attachments/assets/4013ded9-cc42-4e32-9477-3793a7653633" />



# Port-Security

Port-Security is designed to either **protect**, **restrict** or **shutdown** ports when it detects an unregistered/unauthorised device attempting access via a port. 
Port-Security has 2 modes; sticky, static and dynamic. Each of these settings has different functionalities, depending on how secure you want your device, and how critical distruption of service can be. 


Here in this example we have a basic switch setup, with 2 trusted PCs, and a rogue laptop. The rogue laptop will attempt to gain access to the network via the switch, however, the switch has not learned its MAC address an associated it with one of its ports. 
In this simple lab, MAC Address learning is set to **sticky**, and the violation mode is set to **restrict**. for ports f0/1-2. 


<img width="475" height="405" alt="image" src="https://github.com/user-attachments/assets/797e9ce1-022e-47cb-9438-de741f9f79a7" />
<img width="498" height="86" alt="image" src="https://github.com/user-attachments/assets/89e2fb0b-fc4c-42a8-92fc-894989ea0fd7" />

<img width="478" height="415" alt="image" src="https://github.com/user-attachments/assets/44dc6709-e349-4f8f-b3b4-6659f82e1701" />


<img width="436" height="408" alt="image" src="https://github.com/user-attachments/assets/124381c1-2169-4254-8041-b202c92b5a67" />


<img width="392" height="194" alt="image" src="https://github.com/user-attachments/assets/5a8b76e7-7339-4314-bda0-d133dce095d0" />

