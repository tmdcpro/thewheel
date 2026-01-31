// The Wheel - D3.js Visualization Logic (Updated to use embedded data)

const width = window.innerWidth;
const height = window.innerHeight;

// Check if graphData is loaded from data.js
if (typeof graphData !== 'undefined' && graphData.nodes.length > 0) {
    renderViz(graphData);
} else {
    console.log("No dynamic data found. Showing sample graph.");
    const sampleData = {
        nodes: [
            { id: 1, name: "The Wheel", type: "Project", url: "https://github.com" },
            { id: 2, name: "Neo4j", type: "Component" },
            { id: 3, name: "D3.js", type: "Component" }
        ],
        links: [
            { source: 1, target: 2 },
            { source: 1, target: 3 }
        ]
    };
    renderViz(sampleData);
}

function renderViz(data) {
    const svg = d3.select("#viz")
        .append("svg")
        .attr("width", width)
        .attr("height", height)
        .call(d3.zoom().on("zoom", (event) => {
            container.attr("transform", event.transform);
        }));

    const container = svg.append("g");

    const simulation = d3.forceSimulation(data.nodes)
        .force("link", d3.forceLink(data.links).id(d => d.id).distance(100))
        .force("charge", d3.forceManyBody().strength(-300))
        .force("center", d3.forceCenter(width / 2, height / 2));

    const link = container.append("g")
        .attr("class", "links")
        .selectAll("line")
        .data(data.links)
        .enter().append("line")
        .attr("class", "link")
        .attr("stroke-width", 2);

    const node = container.append("g")
        .attr("class", "nodes")
        .selectAll("circle")
        .data(data.nodes)
        .enter().append("circle")
        .attr("class", d => `node node-${(d.type || 'default').toLowerCase()}`)
        .attr("r", d => d.type === "Project" ? 10 : 6)
        .on("mouseover", (event, d) => {
            d3.select("#tooltip")
                .style("display", "block")
                .style("left", (event.pageX + 10) + "px")
                .style("top", (event.pageY - 10) + "px")
                .html(`<strong>${d.name || d.id}</strong><br>Type: ${d.type}`);
        })
        .on("mouseout", () => {
            d3.select("#tooltip").style("display", "none");
        })
        .on("click", (event, d) => {
            if (d.url) {
                window.open(d.url, '_blank');
            } else {
                alert(`Node: ${d.name}\nType: ${d.type}\n(No URL available for this component)`);
            }
        })
        .call(d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended));

    const labels = container.append("g")
        .selectAll("text")
        .data(data.nodes)
        .enter().append("text")
        .text(d => d.name || d.id)
        .attr("dx", 12)
        .attr("dy", 4);

    simulation.on("tick", () => {
        link
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        node
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        labels
            .attr("x", d => d.x)
            .attr("y", d => d.y);
    });

    function dragstarted(event, d) {
        if (!event.active) simulation.alphaTarget(0.3).restart();
        d.fx = d.x;
        d.fy = d.y;
    }

    function dragged(event, d) {
        d.fx = event.x;
        d.fy = event.y;
    }

    function dragended(event, d) {
        if (!event.active) simulation.alphaTarget(0);
        d.fx = null;
        d.fy = null;
    }
}
