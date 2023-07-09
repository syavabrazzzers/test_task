import React from 'react';
import {Page} from "../App";


const Header = ({setPage}: { setPage: (page: Page) => any }) => {
    return (
        <div className={`w-full flex flex-row`}>
            <div onClick={() => setPage(Page.category)} className={`p-2 rounded border m-2`}>Category</div>
            <div onClick={() => setPage(Page.products)} className={`p-2 rounded border m-2`}>Products</div>
        </div>
    );
};

export default Header;