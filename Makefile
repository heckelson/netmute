
SERVICE_DIR := ${HOME}/.config/systemd/user/
SCRIPT_DIR := ${HOME}/Programme/scripts/


install:
	cp ./mute-on-network.service ${SERVICE_DIR}
	mkdir -p ${HOME}/Programme/scripts/
	cp netmute.py ${SCRIPT_DIR}
	

enable:
	systemctl --user enable --now mute-on-network.service
	

restart: install
	systemctl --user enable --now mute-on-network.service
