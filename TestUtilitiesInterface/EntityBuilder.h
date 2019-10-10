#pragma once

namespace systelab { namespace test_utility {

	template<typename _Entity>
	class EntityBuilder
	{
	public:
		EntityBuilder() = default;
		virtual ~EntityBuilder() = default;

		_Entity getEntity() const
		{
			return m_entity;
		}

	protected:
		_Entity m_entity;
	};

}}