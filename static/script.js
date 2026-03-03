async function fetchSystem() {
    const response = await fetch("http://localhost:8000/api/system")
    const data = await response.json()

    document.getElementById("system-data").innerHTML = `
        <div class="row"><span class="label">OS</span><span class="value">${data.os}</span></div>
        <div class="row"><span class="label">VERSION</span><span class="value">${data.os_version}</span></div>
        <div class="row"><span class="label">ARCHITECTURE</span><span class="value highlight">${data.architecture}</span></div>
        <div class="row"><span class="label">HOSTNAME</span><span class="value">${data.hostname}</span></div>
        <div class="row"><span class="label">PROCESSOR</span><span class="value">${data.processor}</span></div>
    `
}

async function fetchCPU() {
    const response = await fetch("http://localhost:8000/api/cpu")
    const data = await response.json()

    document.getElementById("cpu-data").innerHTML = `
        <div class="row"><span class="label">PHYSICAL CORES</span><span class="value">${data.physical_cores}</span></div>
        <div class="row"><span class="label">TOTAL CORES</span><span class="value">${data.total_cores}</span></div>
        <div class="row"><span class="label">CURRENT SPEED</span><span class="value">${data.current_speed}</span></div>
        <div class="row"><span class="label">CPU USAGE</span><span class="value highlight">${data.cpu_usage}</span></div>
    `
}

async function fetchRAM() {
    const response = await fetch("http://localhost:8000/api/ram")
    const data = await response.json()

    document.getElementById("ram-data").innerHTML = `
        <div class="row"><span class="label">TOTAL</span><span class="value">${data.total}</span></div>
        <div class="row"><span class="label">USED</span><span class="value">${data.used}</span></div>
        <div class="row"><span class="label">AVAILABLE</span><span class="value">${data.available}</span></div>
        <div class="row"><span class="label">USAGE</span><span class="value highlight">${data.usage}</span></div>
        <div class="row"><span class="label">SWAP TOTAL</span><span class="value">${data.swap_total}</span></div>
        <div class="row"><span class="label">SWAP USED</span><span class="value">${data.swap_used}</span></div>
        <div class="row"><span class="label">SWAP USAGE</span><span class="value highlight">${data.swap_usage}</span></div>
    `
}

async function fetchDisk() {
    const response = await fetch("http://localhost:8000/api/disk")
    const data = await response.json()

    let partitionsHTML = ""
    data.partitions.forEach(partition => {
        partitionsHTML += `
            <div class="interface-block">
                <div class="row"><span class="label">MOUNTPOINT</span><span class="value highlight">${partition.mountpoint}</span></div>
                <div class="row"><span class="label">FILESYSTEM</span><span class="value">${partition.filesystem}</span></div>
                <div class="row"><span class="label">TOTAL</span><span class="value">${partition.total}</span></div>
                <div class="row"><span class="label">USED</span><span class="value">${partition.used}</span></div>
                <div class="row"><span class="label">FREE</span><span class="value">${partition.free}</span></div>
                <div class="row"><span class="label">USAGE</span><span class="value highlight">${partition.usage}</span></div>
            </div>
        `
    })

    document.getElementById("disk-data").innerHTML = `
        ${partitionsHTML}
        <div class="row"><span class="label">TOTAL READ</span><span class="value">${data.total_read}</span></div>
        <div class="row"><span class="label">TOTAL WRITTEN</span><span class="value">${data.total_written}</span></div>
        <div class="row"><span class="label">READ OPS</span><span class="value">${data.read_ops}</span></div>
        <div class="row"><span class="label">WRITE OPS</span><span class="value">${data.write_ops}</span></div>
    `
}

async function fetchNetwork() {
    const response = await fetch("http://localhost:8000/api/network")
    const data = await response.json()

    let interfacesHTML = ""
    data.interfaces.forEach(iface => {
        interfacesHTML += `
            <div class="interface-block">
                <div class="row"><span class="label">INTERFACE</span><span class="value highlight">${iface.interface}</span></div>
                <div class="row"><span class="label">IP ADDRESS</span><span class="value">${iface.ip_address}</span></div>
                <div class="row"><span class="label">SUBNET MASK</span><span class="value">${iface.subnet_mask}</span></div>
            </div>
        `
    })

    document.getElementById("network-data").innerHTML = `
        ${interfacesHTML}
        <div class="row"><span class="label">BYTES SENT</span><span class="value">${data.bytes_sent}</span></div>
        <div class="row"><span class="label">BYTES RECEIVED</span><span class="value">${data.bytes_received}</span></div>
        <div class="row"><span class="label">PACKETS SENT</span><span class="value">${data.packets_sent}</span></div>
        <div class="row"><span class="label">PACKETS RECEIVED</span><span class="value">${data.packets_received}</span></div>
    `
}

async function fetchAll() {
    await fetchSystem()
    await fetchCPU()
    await fetchRAM()
    await fetchDisk()
    await fetchNetwork()
}

fetchAll()
setInterval(fetchAll, 2000)