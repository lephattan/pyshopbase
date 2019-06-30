class ApiResponse:
    def __init__(self, r):
        self.raw_respone = r
        self.json = {}
        self.status = ''
        self.status_code = None
        if r.status_code == 200:
            self.status = 'success'
            self.status_code = r.status_code
            self.json = r.json()
        elif r.status_code == 503:
            self.status_code = 'fail'
            self.status_code = r.status_code
            self.json = {'message': r.content}
        else:
            self.status_code = 'fail'
            self.status_code = r.status_code
            self.json = {'message': r.content}
