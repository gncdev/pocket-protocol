import all


class ActorPickRequestPacket(all, all.DataPacket):
	NETWORK_ID = ProtocolInfo.ACTOR_PICK_REQUEST_PACKET
	
	
	def decodePayload(self):
		self.entityUniqueId = self.getLLong(self)
		self.hotbarSlot = self.getByte(self)
	
	
	def encodePayload(self):
		self.putLLong(self.entityUniqueId)
		self.putByte(self.hotbarSlot)
	
	
	def handle(self, session: NetworkSession) -> bool:
		return session.handleActorPickRequest(self)
