import { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/v1';

const useApi = (method, endpoint, requestData = null, requestHeaders = null) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [shouldFetch, setShouldFetch] = useState(false);

  

  useEffect(() => {
    if (!shouldFetch) return;

    console.log(requestData)

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
        setShouldFetch(false); // Reset after fetching
      }
    };

    fetchData();
  }, [shouldFetch, method, endpoint, requestData, requestHeaders]);

  const triggerFetch = () => setShouldFetch(true);

  return { data, loading, error, triggerFetch };
};

export default useApi;