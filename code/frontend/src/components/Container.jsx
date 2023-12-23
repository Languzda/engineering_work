import { PropTypes } from "prop-types";

import "./Container.css";

const MAX_BLOCKS = 15;

const Container = ({ dane }) => {
  const numberOfContainer = dane.container_id;
  const numberOfBlocks = dane.container_blocks;
  const numberOfBlocksToShow =
    numberOfBlocks > MAX_BLOCKS ? MAX_BLOCKS : numberOfBlocks;

  const blocksFull = [];
  for (let i = 0; i < numberOfBlocksToShow; i++) {
    blocksFull.push(
      <div
        key={`${numberOfContainer}${i}F`}
        className="container-block block-full"
      ></div>
    );
  }

  const blocksEmpty = [];
  for (let i = 0; i < MAX_BLOCKS - numberOfBlocksToShow; i++) {
    blocksEmpty.push(
      <div
        key={`${numberOfContainer}${i}E`}
        className="container-block block-empty"
      ></div>
    );
  }

  const blocks = [...blocksEmpty, ...blocksFull];

  return (
    <div className="container">
      <div className="container-header">
        <h2>Pojemnik: {numberOfContainer}</h2>
      </div>
      <div className="container-header">
        <p>Ilość bloków w pojemniku: {numberOfBlocks}</p>
      </div>
      <div className="container-blocks">{blocks}</div>
    </div>
  );
};

Container.propTypes = {
  dane: PropTypes.shape({
    container_id: PropTypes.number.isRequired,
    container_blocks: PropTypes.number.isRequired,
    container_name: PropTypes.string,
  }).isRequired,
};

export default Container;
