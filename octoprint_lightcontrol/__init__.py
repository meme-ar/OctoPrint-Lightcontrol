# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import serial

import flask

    
class LightControlPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.SimpleApiPlugin,
                       octoprint.plugin.AssetPlugin):

    def lightswitch(self, port):
        new_status = 1 if self._settings.get(["status"]) == 0 else 0

        octoprint.plugin.SettingsPlugin.on_settings_save(self, dict(status=new_status))
        
        arduino = serial.Serial(port=port, baudrate=115200, timeout=.1)
        arduino.write(bytes(self._settings.get(["status"]), 'utf-8'))

        self._logger.info(f'switch {port}, {new_status}')

    def on_after_startup(self):
        self._logger.info('Light control plugin loaded')

    # settings
    def get_settings_defaults(self):
        return dict(port="COM4", status=0)

    # templates
    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]
    # js
    def get_assets(self):
        return dict(
            js=['js/lightcontrol.js'],
         )

    # api
    def get_api_commands(self):
        return dict(
            toggle=[]
        )

    def on_api_command(self, command, data):
        self.lightswitch(self._settings.get(["port"]))
        return flask.jsonify(status=self._settings.get(["status"]))

    def on_api_get(self, request):
        return flask.jsonify(status=self._settings.get(["status"]))


__plugin_name__ = "Light Control"
__plugin_pythoncompat__ = ">=2.7,<4"
__plugin_implementation__ = LightControlPlugin()
