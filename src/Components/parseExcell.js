import React from 'react';
import XLSX from "xlsx";

export const ParseExcell = () => {

    const handleFile = async (e) => {
        const file = e.target.files[0];
        const data = await file.arrayBuffer();
        const workbook = XLSX.read(data);
        const worksheet = workbook.Sheets[workbook.SheetNames[0]];
        const jsonData = XLSX.utils.sheet_to_json(worksheet);

        console.log(jsonData);
    }
   
  return (
    <>
    <h1>Give the Input File</h1>
    <input type="file" onChange={(e) => handleFile(e)}/>
    </>
  )
}

