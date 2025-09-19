import React from "react";
const Home: React.FC = () => <div><h1>Welcome</h1><p>Public landing page.</p></div>;
export default Home;
import React from 'react';
import Layout from '../templates/Layout/Layout';

const Home: React.FC = () => {
    return (
        <Layout>
            <h1>Welcome to the School Site</h1>
            <p>This is the landing page of the application.</p>
        </Layout>
    );
};

export default Home;