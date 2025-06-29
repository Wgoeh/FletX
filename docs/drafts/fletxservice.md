# FletXService
**Example Usage**
```python
# Exemple d'implémentation concrète
class APIService(FletXService):
    """Exemple de service API utilisant FletXService"""
    
    def __init__(self, base_url: str, **kwargs):
        self.base_url = base_url
        super().__init__(**kwargs)
    
    def on_start(self):
        """Initialisation du service API"""
        self.set_data('base_url', self.base_url)
        self.log_info(f"API Service initialized with base URL: {self.base_url}")
    
    async def fetch_data(self, endpoint: str) -> Dict[str, Any]:
        """Exemple de méthode utilisant le client HTTP"""
        if not self.is_ready:
            raise RuntimeError("Service not ready")
        
        if self.http_client:
            # Utilisation du client HTTP FletX
            url = f"{self.base_url}/{endpoint}"
            response = await self.http_client.get(url)
            return response
        else:
            # Simulation sans client HTTP
            self.log_info(f"Fetching data from {endpoint}")
            return {"data": f"Mock data from {endpoint}"}


# Exemple d'utilisation
if __name__ == "__main__":
    # Service synchrone
    api_service = APIService("https://api.example.com", name="ExampleAPI")
    
    # Ajouter des listeners
    api_service.on('ready', lambda _: print("Service is ready!"))
    api_service.on('error', lambda error: print(f"Service error: {error}"))
    
    print(api_service)
    print(f"Is ready: {api_service.is_ready}")
    print(f"Data: {api_service.data}")

```