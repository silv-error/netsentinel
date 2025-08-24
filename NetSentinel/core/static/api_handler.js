async function get_data_from_api() {
  try {
    const response = await fetch("http://127.0.0.1:8001/api/device_data");

    if (!response.ok) {
      throw new Error("HTTP error " + response.status);
    }

    const result = await response.json();
    console.log("Received Status:", result);
  } catch (err) {
    console.error("Fetch error:", err);
  }
}

get_data_from_api();
