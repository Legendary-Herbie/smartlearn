import React from 'react';

const Footer: React.FC = () => {
    return (
        <footer style={{ textAlign: 'center', padding: 12, borderTop: '1px solid #eee' }}>
            © School Site {new Date().getFullYear()}
        </footer>
    );
};

export default Footer;