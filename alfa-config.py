from __builtin__ import any as is_any
import os


start_up_dir = "/etc/rc.local"

# function to discover wlan interface dynamically, if only 1 wireless iface exists, use that - otherwise default to the very last wireless iface.
def find_wlan():
	net_ifaces = os.listdir("/sys/class/net")
	wireless_iface = "wlan"
	test_wlan = is_any(wireless_iface in i for i in net_ifaces)
	if test_wlan is True:
		wlan_ifaces = [j for j in net_ifaces if wireless_iface in j]
		print "\n WLAN Interface(s) found as: "
		for x in wlan_ifaces:
			print "\t %s" % x
		num_ifaces = len(wlan_ifaces)
		if num_ifaces is 1:
			wlan_result = str(wlan_ifaces[0])
			print "\n Utilizing: %s" % wlan_result
			return wlan_result
		elif num_ifaces != 0 and num_ifaces != 1:
			wlan_result = str(wlan_ifaces[num_ifaces - 1])
			print "\n Utilizing last wlan interface: %s" % wlan_result
			return wlan_result
		else:
			print "\n No interfaces listed."

	else:
		print "\n No wireless interface could be found...Exiting configuration script."
		exit(1)

wlan_result = find_wlan()
print wlan_result



exit(0)