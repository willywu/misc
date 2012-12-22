#Instructions

How to setup an AWS machine that runs OpenVPN.  Generally started from http://holgr.com/blog/2009/06/setting-up-openvpn-on-amazons-ec2/

#Setup the AWS machine
1. Sign up a machine.  I used the Amazon Linux AMI.  I didn't use Ubuntu because of its UFW.
2. SSH into it, i.e. ssh -i {pem_file} ec2-user@{location}.  Then sudo su
3. yum update
4. yum install openvpn
5. Make a secret pre-shared key in /etc/openvpn: openvpn —genkey —secret /etc/openvpn/openvpn-key.txt
6. Put openvpn.conf into /etc/openvpn
7. service openvpn restart

#Setup the client
1. Download Tunnelblick
2. Copy the openvpn-key.txt from the server into client's openvpn/config directory
3. Update AmazonEC2.ovpn, copy both into Tunnelblick's private configs folder

#Setup the AWS machine - Part II
1. Create/append to /etc/sysconfig/iptables
    *nat
    :POSTROUTING ACCEPT [0:0]
    :PREROUTING ACCEPT [0:0]
    :OUTPUT ACCEPT [0:0]
    -A POSTROUTING -s 192.168.2.0/24 -d 0.0.0.0/0 -o eth0 -j MASQUERADE
    COMMIT
2. service iptables restart
3. Enable ip forwarding in openvpn by editing /etc/init.d/openvpn and uncommenting
    echo 1 > /proc/sys/net/ipv4/ip_forward
4. service openvpn restart
