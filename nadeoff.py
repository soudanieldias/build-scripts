def apply_script(protocol,connection,config): 

    class NonadeConnection(connection):
        def on_hit(self, hit_amount, hit_player, type, grenade): 
            if grenade:
                return False
            return connection.on_hit(self, hit_amount, hit_player, type, grenade)

    return protocol, NonadeConnection
