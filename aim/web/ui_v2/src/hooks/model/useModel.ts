import React from 'react';
import { IModel } from 'types/services/models/model';

function useModel<StateType>(model: IModel<StateType>): StateType | null {
  const [state, setState] = React.useState<StateType | null>(model.getState());

  React.useEffect(() => {
    const initSubscription = model.subscribe('INIT', () =>
      setState(model.getState()),
    );
    const updateSubscription = model.subscribe('UPDATE', () =>
      setState(model.getState()),
    );

    return () => {
      model.destroy();
      initSubscription.unsubscribe();
      updateSubscription.unsubscribe();
    };
  }, []);

  return state;
}

export default useModel;
