# BasicNetworkSecurity

This is a set of basic network security tasks!

# Passwords

### 🔐 Password Security Demonstration: Type 5 (MD5) vs Type 9 (scrypt)
This network lab includes hands-on demonstrations of two Cisco password encryption schemes:
- Type 5: Legacy MD5-based hashing
- Type 9: Modern scrypt-based hashing, offering stronger resistance to brute-force attacks

<img width="508.2" height="323.4" alt="image" src="https://github.com/user-attachments/assets/5d43886b-8af3-4cea-bc54-faeaa6341ae1" />

<img width="306.6" height="280.7" alt="image" src="https://github.com/user-attachments/assets/cb95c7a4-2aa0-47c9-b9ef-0aa975a81e65" />

Both methods are used to secure local passwords on Cisco devices, depending on hardware and IOS version compatibility.
💡 Why Use Type 9?
Where supported, Type 9 (scrypt) should always be preferred:
- Designed for password hardening
- Computationally intensive and memory-bound
- Far more resilient against dictionary and brute-force attacks than MD5
However, in some environments — such as older IOS versions or constrained hardware — Type 9 may not be available. In those cases, Type 5 (MD5) remains a fallback option.
This lab contains one example of each, allowing for comparison of syntax, behavior, and configuration within a simulated network environment.






<img width="562" height="222" alt="image" src="https://github.com/user-attachments/assets/0d90a547-9184-4d73-b0d2-1e48d4c16c0f" />
<img width="643" height="46" alt="image" src="https://github.com/user-attachments/assets/b6683a69-cff9-4bcd-a6f8-a8387731db07" />



# VLANS

## 🔒 Basic Security Activities – VLAN Segmentation
This lab demonstrates foundational network security practices through VLAN-based segmentation across a multi-site topology.
To enhance both efficiency and security, devices are grouped into logical domains using dedicated VLANs. For instance, only devices within the Management VLAN receive administrative traffic, while Phones, Wi-Fi clients, and User PCs operate within isolated VLANs tailored to their roles.

<img width="988" height="576" alt="image" src="https://github.com/user-attachments/assets/0d44e74c-4365-4f68-9bb5-939624de279d" />
## 📷 Visual Overview
The diagram showcases two distinct office environments (A & B), each populated with access switches, phones, laptops, and wireless access points. This segmentation ensures traffic is properly separated, enhances fault isolation, and supports scalability.
<img width="656" height="306" alt="image" src="https://github.com/user-attachments/assets/4013ded9-cc42-4e32-9477-3793a7653633" />




# Port-Security


## 🔐 Port Security Lab Summary

This lab aims to demonstrate how Cisco switch port security can prevent unauthorized access using sticky MAC address learning and the restrict violation mode.
### Lab Setup:
- Switch: Basic Layer 2 switch
- Trusted Devices: PC1 and PC2 connected to ports f0/1 and f0/2
- Rogue Device: Unregistered laptop attempting access
- Configuration:
- MAC address learning: sticky
- Violation mode: restrict
- Ports secured: f0/1 and f0/2
### Expected Behavior:
- The switch learns and stores the MAC addresses of PC1 and PC2.
- When the rogue laptop connects, its MAC address doesn’t match the stored entries.
- Because the violation mode is set to restrict, the switch:
- Drops packets from the rogue device
- Logs the violation
- Increments the security violation counter
- Does not shut down the port (unlike shutdown mode)

<img width="475" height="405" alt="image" src="https://github.com/user-attachments/assets/797e9ce1-022e-47cb-9438-de741f9f79a7" />

Port-Security is designed to either **protect**, **restrict** or **shutdown** ports when it detects an unregistered/unauthorised device attempting access via a port. 
Port-Security has 3 modes; sticky, static and dynamic. Each of these settings has different functionalities, depending on how secure you want your device, and how critical distruption of service can be. 


Here in this example we have a basic switch setup, with 2 trusted PCs, and a rogue laptop. The rogue laptop will attempt to gain access to the network via the switch, however, the switch has not learned its MAC address an associated it with one of its ports. 
In this simple lab, MAC Address learning is set to **sticky**, and the violation mode is set to **restrict**. for ports f0/1-2. 

<img width="498" height="86" alt="image" src="https://github.com/user-attachments/assets/89e2fb0b-fc4c-42a8-92fc-894989ea0fd7" />


<img width="392" height="194" alt="image" src="https://github.com/user-attachments/assets/5a8b76e7-7339-4314-bda0-d133dce095d0" />

Then, when a device tries to connect to one of these ports, the switch will have learned the MAC address of the authorised device depending on the MAC address learning method, and it will go in it's MAC address table. When the new device is connected to this port, the switch will compare this device to it's MAC address, and if the entries don't match, it will act depending on the violation mode it is set to. In this case, **Restrict**




