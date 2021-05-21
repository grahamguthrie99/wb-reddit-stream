import alpaca_trade_api as Alpaca

class Universe:
    def __init__(self, alpaca_client_id, alpaca_client_secret, alpaca_endpoint):
        self.alpaca_client_id = alpaca_client_id
        self.alpaca_client_secret = alpaca_client_secret
        self.alpaca_endpoint = alpaca_endpoint
        self.api = self._create_connection()
        self.asset_list, self.asset_table = self._build_asset_universe()
    
    def _create_connection(self):
        return Alpaca.REST(
            self.alpaca_client_id, 
            self.alpaca_client_secret,
            base_url=self.alpaca_endpoint)
                   
    def _build_asset_universe(self): 
        asset_list = []
        asset_table = {}
        for asset in self.api.list_assets():
            if asset.status == 'active' and asset.tradable and asset.easy_to_borrow:
                asset_list.append(asset.symbol)
                asset_table[asset.symbol] = [asset.exchange, asset.name]
        return asset_list, asset_table
    


