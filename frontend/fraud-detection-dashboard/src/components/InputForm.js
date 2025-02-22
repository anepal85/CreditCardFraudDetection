import React from "react";

function InputForm({ inputData, setInputData, onPredict, setDefaults }) {
  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    onPredict(inputData);
  };

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputData({ ...inputData, [name]: parseFloat(value) });
  };

  return (
    <div className="input-form">
      <h2>Make a Prediction</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(inputData).map((key) => (
          <div key={key}>
            <label>{key}</label>
            <input
              type="number"
              name={key}
              value={inputData[key]}
              onChange={handleChange}
              step="0.01"
            />
          </div>
        ))}
        <button type="button" onClick={setDefaults}>Set Defaults</button>
        <button type="submit">Predict</button>
      </form>
    </div>
  );
}

export default InputForm;