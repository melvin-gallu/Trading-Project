import { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const useApi = (method, endpoint, requestData = null, requestHeaders = null) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError(null);
      try {
        const response = await axios({
          method: method,
          url: `${API_BASE_URL}${endpoint}`,
          data: requestData,
          headers: requestHeaders,
        });
        setData(response.data);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [method, endpoint,requestData, requestHeaders]);

  return { data, loading, error };
};


export default useApi;