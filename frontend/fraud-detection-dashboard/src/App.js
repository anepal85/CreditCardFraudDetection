import React, { useState, useEffect } from "react";
import axios from "axios";
import InputForm from "./components/InputForm";
import Chart from "./components/Chart";
import "./App.css";

function App() {
  const [testData, setTestData] = useState([]);
  const [predictions, setPredictions] = useState([]);
  const [inputData, setInputData] = useState({});

  // Fetch test data from FastAPI
  useEffect(() => {
    axios.get("http://localhost:8000/test_data")
      .then((response) => {
        const csvData = response.data;
        const rows = csvData.split("\n");
        const headers = rows[0].split(",");
        const data = rows.slice(1).map((row) => {
          const values = row.split(",");
          return headers.reduce((obj, header, index) => {
            obj[header] = parseFloat(values[index]);
            return obj;
          }, {});
        });
        setTestData(data);

        // Fetch predictions for the entire test dataset
        axios.post("http://localhost:8000/predict_batch", { data })
          .then((response) => {
            setPredictions(response.data.predictions);
          })
          .catch((error) => console.error("Error fetching predictions:", error));
      })
      .catch((error) => console.error("Error fetching test data:", error));
  }, []);

  // Handle single prediction
  const handlePredict = (input) => {
    axios.post("http://localhost:8000/predict", input)
      .then((response) => {
        setPredictions([...predictions, response.data.prediction]);
      })
      .catch((error) => console.error("Error making prediction:", error));
  };

  // Set defaults from the first row of test data
  const setDefaults = () => {
    if (testData.length > 0) {
      const defaults = { ...testData[0] };
      delete defaults.Class; // Remove the target column
      setInputData(defaults);
    }
  };

  return (
    <div className="App">
      <h1>Fraud Detection Dashboard</h1>
      <div className="dashboard">
        <div className="row">
          <InputForm inputData={inputData} setInputData={setInputData} onPredict={handlePredict} setDefaults={setDefaults} />
        </div>
        <div className="row">
          <Chart testData={testData} predictions={predictions} />
        </div>
      </div>
    </div>
  );
}

export default App;