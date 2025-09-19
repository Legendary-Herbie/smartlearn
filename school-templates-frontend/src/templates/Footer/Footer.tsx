import React from "react";

const Footer: React.FC = () => <footer style={{ textAlign: "center", padding: 12, borderTop: "1px solid #eee" }}>© School Site</footer>;
export default Footer;
import React from 'react';

const Footer: React.FC = () => {
    return (
        <footer>
            <div>
                <p>&copy; {new Date().getFullYear()} School Site. All rights reserved.</p>
            </div>
        </footer>
    );
};

export default Footer;