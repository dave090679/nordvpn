# flixgrab app module
import appModuleHandler
from NVDAObjects.UIA import UIA, ListItem
class nordvpncontainer(UIA):
	def _get_name(self):
		return self.firstChild.firstChild.name


class nordvpnlistitem(ListItem):
	def _get_name(self):
		return self.children[2].name

class flixgrabobj(UIA):
	def _get_name(self):
		return self.UIAElement.cachedAutomationId.split(".")[-1]

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.name == ""  and isinstance(obj, UIA):
				clslist.insert(0, flixgrabobj)
		elif obj.name in ["NordVpn.Application.Core.ViewModels.SidePanel.SidePanelRecentViewModel", "NordVpn.Application.Core.ViewModels.Servers.CategoryViewModel", "NordVpn.Application.Core.ViewModels.Servers.CountryViewModel", "NordVpn.Application.Core.ViewModels.Search.SearchGroupResultViewModel"]:
			clslist.insert(0, nordvpnlistitem)
		elif obj.name in ["NordVpn.Application.Core.ViewModels.Settings.SettingsContainerViewModel", "NordVpn.Application.Core.ViewModels.Settings.AutoConnect.AutoConnectSettingViewModel", "NordVpn.Application.Core.ViewModels.Settings.KillSwitch.KillSwitchSettingsContainerViewModel", "NordVpn.Application.Core.ViewModels.Settings.AdvancedSettings.AdvancedSettingsViewModel", "NordVpn.Application.Core.ViewModels.Settings.MyAccountViewModel"]:
			clslist.insert(0, nordvpncontainer)
