import { useState } from 'react';
import useApi from './FastapiRest';

const Form = () => {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');

  const user = {username:firstName, full_name:lastName}

  const { data, loading, error, triggerFetch } = useApi(
    'POST', 
    '/form/test', 
    user
  );

  const onSubmit = (e) => {
    e.preventDefault();
    triggerFetch(); // Trigger the API call
  };

  return (
    <form onSubmit={onSubmit}>
      <label>
        First name:
        <input 
          name="firstName"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
        />
      </label>
      <label>
        Last name:
        <input 
          name="lastName"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
        />
      </label>
      <button type="submit">Submit</button>

      {loading && <p>Loading...</p>}
      {error && <p>Error: {error.message}</p>}
      {error && <p>Detail: {JSON.stringify(error.response)}</p>}
      {data && <p>Response: {JSON.stringify(data)}</p>}
    </form>
  );
}

export default Form;
