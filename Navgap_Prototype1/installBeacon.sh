#! /bin/bash
# This script will ask the user the name of the wireless interface, Hotspot SSID and the corresponding pass$

#echo "Type the name of your wireless interface and press [ENTER]"

#read intwifi

echo "Type the name that you want your hotspot to broadcast and press [ENTER]"

read hotspotname

echo "Type the password(between 8 and 18characters)  for the hotspot"

read hotspotpassword

echo "Wifi interface: $intwifi"
echo "Hotspot name  : $hotspotname"
echo "password      : $hotspotpassword"
echo ""
echo "Configuring Hostapd"
sudo mv /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.bak
sudo touch /etc/hostapd/hostapd.conf
echo "interface=wlan0
driver=nl80211
ssid=$hotspotname
hw_mode=g
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=2
wpa=2
wpa_passphrase=$hotspotpassword
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
ieee80211n=1          # 802.11n support
wmm_enabled=1         # QoS support
ht_capab=[HT40][SHORT-GI-20][DSSS_CCK-40]" >> /etc/hostapd/hostapd.conf

sudo mv /etc/default/hostapd /etc/default/hostapd.bak
sudo touch /etc/default/hostapd/
sudo echo 'DAEMON_CONF="/etc/hostapd/hostapd.conf"'
echo "Hostapd done!"
echo "Configuring udhcpd"
sudo mv /etc/udhcpd.conf /etc/udhcpd.conf.bak
sudo touch /etc/udhcpd.conf
sudo echo 'start 192.168.42.2 # This is the range of IPs that the hostspot will give to client devices.
end 192.168.42.20
interface wlan0 # The device uDHCP listens on.
remaining yes
maxleases 10
opt dns 8.8.8.8 4.2.2.2 # The DNS servers client devices will use.
opt subnet 255.255.255.0 # The subnet of the network, currently allowing 254 hosts total
opt router 192.168.42.1 # The IP address on wlan0 which we will set up shortly.##cmd not found line 55
opt lease 864000 # 10 day DHCP lease time in seconds
' >> /etc/udhcpd.conf

sudo mv /etc/default/udhcpd /etc/default/udhcpd.bak
sudo touch /etc/default/udhcpd
sudo echo '#DHCPD_ENABLED=”no”' >> /etc/default/udhcpd

sudo ifconfig wlan 192.168.42.1
sudo mv /etc/network/interfaces /etc/network/interfaces.bak
sudo touch /etc/network/interfaces
sudo echo "source-directory
auto lo
iface lo inet loopback

iface eth0 inet manual
iface wlan0 inet static
address 192.168.42.1
netmask 255.255.255.0

allow-hotplug wlan1
iface wlan1 inet manual
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
" >> /etc/network/interfaces

sudo echo 'Making changes to /etc/rc.local'
sudo mv /etc/rc.local /etc/rc.local.bak
sudo touch /etc/rc.local
sudo echo '#!/bin/sh -e
#
# rc.local
sudo /srv/navgap/Beacon.sh start
sudo ifconfig wlan0 192.168.42.1
exit 0' >> /etc/rc.local

sudo systemctl start udhcpd
sudo systemctl start hostapd
sudo systemctl enable udhcpd
sudo systemctl enable hostapd
