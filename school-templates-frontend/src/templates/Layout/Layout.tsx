import React from 'react';
import Header from '../Header/Header';
import Footer from '../Footer/Footer';

const Layout: React.FC<{ children?: React.ReactNode }> = ({ children }) => {
    return (
        <div>
            <Header />
            <main style={{ padding: 16 }}>{children}</main>
            <Footer />
        </div>
    );
};

export default Layout;