from aoc.snd.netconfsnd import NetconfSND

from aoc.snd.snd_model_pb2.sysoidinfo_pb2 import SysoidInfo
from aoc.snd.snd_model_pb2.connectinfo_pb2 import ConnectInfos, ProtocolEntity, DEFAULT_CONNECT, PRIMARY_CONNECTION, \
    HelloEntity
from aoc.snd.snd_model_pb2.channelInfo_pb2 import SINGLE_CHANNEL
from aoc.snd.snd_model_pb2.ecsdriver_pb2 import CommonDriverInfo, NetconfDriverInfo


class SND(NetconfSND):
    def getSysoidInfo(self, aoccontext, request=None):
        self.logger.info('getSysoidInfo start.')
        sysoidInfo = SysoidInfo()
        sysoidEntity = sysoidInfo.sysoidEntity.add()
        sysoidEntity.sysoid = "1.3.6.1.4.1.2011.2.62.2.8"
        sysoidEntity.deviceType = "ROUTER"
        sysoidEntity.deviceModel = "NE40E-X3"
        sysoidEntity.deviceVendor = "HUAWEI"
        self.logger.info('getSysoidInfo end.')
        return sysoidInfo

    def getConnectInfo(self, aoccontext, request=None):
        self.logger.info('getConnectInfo start.')
        connectInfos = ConnectInfos()
        connectInfo = connectInfos.connectInfo.add()
        connectInfo.protocolEntity.protocolType = ProtocolEntity.netconf
        connectInfo.protocolEntity.helloEntity.helloType = HelloEntity.extendType
        connectInfo.connectPolicy = DEFAULT_CONNECT
        connectInfo.channelInfo.readChannel = SINGLE_CHANNEL
        connectInfo.channelInfo.is_read_share_write = True
        connectInfo.connectionPriority = PRIMARY_CONNECTION
        self.logger.info('getConnectInfo end.')
        return connectInfos

    def getCommonDriverInfo(self, aoccontext, request=None):
        self.logger.info('getCommonDriverInfo start.')
        common_driver = CommonDriverInfo()
        common_driver.unsupportedOperations = "create"
        common_driver.deleteStrategy = 1
        syncToDel = common_driver.para.add()
        syncToDel.key = "sync-to-del-enable"
        syncToDel.value = "true"
        self.logger.info('getCommonDriverInfo end.')
        return common_driver

    def getNetconfDriverInfo(self, aoccontext, request=None):
        self.logger.info('getNetconfDriverInfo start.')
        netconf_driver = NetconfDriverInfo()
        netconf_driver.phase = "two"
        netconf_driver.classification = "huawei-v5"
        #netconf_driver.testOption = "set"
        self.logger.info('getNetconfDriverInfo end.')
        return netconf_driver

