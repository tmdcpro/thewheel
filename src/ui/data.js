const graphData = {
  "nodes": [
    {
      "id": 1,
      "name": "twbs/bootstrap",
      "type": "Project",
      "url": "https://github.com/twbs/bootstrap"
    },
    {
      "id": 2,
      "name": "fastapi/fastapi",
      "type": "Project",
      "url": "https://github.com/fastapi/fastapi"
    },
    {
      "id": 3,
      "name": "REST API",
      "type": "Project",
      "url": "https://github.com/fastapi/fastapi"
    },
    {
      "id": 4,
      "name": "gin-gonic/gin",
      "type": "Project",
      "url": "https://github.com/gin-gonic/gin"
    }
  ],
  "links": [
    {
      "source": 1,
      "target": 2
    },
    {
      "source": 2,
      "target": 3
    },
    {
      "source": 3,
      "target": 4
    },
    {
      "source": 3,
      "target": 4
    },
    {
      "source": 3,
      "target": 4
    }
  ]
};