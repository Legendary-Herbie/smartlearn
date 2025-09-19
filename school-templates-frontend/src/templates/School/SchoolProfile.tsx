import React, { useEffect, useState } from "react";
import api from "../../services/api";

const Profile: React.FC = () => {
  const [profile, setProfile] = useState<any>(null);
  useEffect(() => {
    api.me().then((r) => setProfile(r.data)).catch(() => {});
  }, []);
  if (!profile) return <div>Loading...</div>;
  return (
    <div>
      <h2>{profile.username}'s Profile</h2>
      <img src={profile.profile_picture} alt="avatar" style={{ width: 120 }} />
      <p>Email: {profile.email}</p>
    </div>
  );
};
export default Profile;
import React from 'react';

const SchoolProfile: React.FC = () => {
    return (
        <div>
            <h1>School Profile</h1>
            <p>Details about the school will be displayed here.</p>
        </div>
    );
};

export default SchoolProfile;