import '../styles/ButtonLink.css';

function ButtonLink({ to, children }) {
    return (
        <a href={to} className="btn_sub">{children}</a>
    );
}

export default ButtonLink;